'''
ctrl + f 를 눌러 "개인 수정" 이라고 검색하여, 자신의 네트워크에 맞게 변경 필요
'''

## 라이브러리 설치하기 
# pip install sqlalchemy
# pip install streamlit
# pip install plotly
# pip install streamlit-autorefresh
# pip install pymysql

from sqlalchemy import create_engine
import streamlit as st
from streamlit_autorefresh import st_autorefresh
import pandas as pd
import plotly.express as px

from hyori_function import *
from seungbin_function import *
from juyeong_function import *
from himchan_function import *

# -----------------------------------------------------------
# 1. RDBMS 정보 : 수정
# -----------------------------------------------------------
SERVER_IP = "localhost"   # 개인 수정
USER_ID = "root"           # 개인 수정
USER_PW = "mysql"           # 개인 수정
DB_NAME = "projectdb"
CHARSET = "utf8mb4"

## mysql -> sqlAlchemy -> pandas 위한 변수
ENGINE = create_engine(
    f"mysql+pymysql://{USER_ID}:{USER_PW}@{SERVER_IP}/{DB_NAME}?charset=utf8mb4"
)

# 모듈별 테이블 매핑
MODULE_TABLE_MAP = {
    "Module_A": "modulea_tbl",
    "Module_B": "moduleb_tbl",
    "Module_C": "modulec_tbl",
    "Module_D": "moduled_tbl",
    "Module_E": "modulee_tbl"
}

# -----------------------------------------------------------
# 2. 페이지 설정 및  전체 CSS 설정
# -----------------------------------------------------------
st.set_page_config(page_title="BMS Dashboard", page_icon="🔋", layout="wide")

st.markdown("""
<style>
    /* 전체 페이지 배경: 하늘색 파스텔 */
    .stApp {
        background-color: #E0F7FA; 
    }
    
    /* 상단 여백 */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* 왼쪽 컬럼 (연보라색 박스) */
    [data-testid="stSidebarContent"] {
    }
    
    div[data-testid="column"]:nth-of-type(1) > div {
        background-color: #E8DAFF;
        border-radius: 20px;
        padding: 20px;
        box-shadow: 4px 4px 10px rgba(0,0,0,0.1);
        height: 100%;
        border: 1px solid #D1C4E9;
    }

    /* 오른쪽 컬럼 (흰색 박스) */
    div[data-testid="column"]:nth-of-type(2) > div {
        background-color: #FFFFFF;
        border-radius: 20px;
        padding: 20px;
        box-shadow: 4px 4px 10px rgba(0,0,0,0.1);
        height: 100%;
    }

    /* 폰트 */
    body { font-family: 'Poppins', sans-serif; }
    
    /* 상태 박스 */
    .status-box-inner {
        border-radius: 12px;
        padding: 15px;
        margin-top: 10px;
        margin-bottom: 15px;
        text-align: center;
        font-weight: bold;
        border: 2px solid #1E90FF;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------
# 3. 이상치 탐지 함수
# -----------------------------------------------------------
def detect_anomaly(df_row):
    """
    row 기준으로 이상치 여부 판단
    True → 이상치
    False → 정상
    """
    if df_row['cell_temperature_c'] < 28 :
        return True

    return False



# -----------------------------------------------------------
# 4. DB에서 데이터 가져오기 함수
# -----------------------------------------------------------
def load_data_from_mysql(increment: bool = False, data_limit: int = 0, last_row: int = 70) -> pd.DataFrame:
    frames = []
    try:
        for module_id, table_name in MODULE_TABLE_MAP.items():
            query = f"""
                SELECT *
                FROM {table_name}
                ORDER BY timestamp ASC 
                LIMIT {last_row} OFFSET {data_limit}
            """
            try:
                df = pd.read_sql(query, ENGINE)
            except Exception as e:
                st.error(f"테이블 `{table_name}` 조회 중 오류: {e}")
                continue
            if df.empty:
                continue
            df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")  # 데이터 형변환
            df["module_id"] = module_id
            frames.append(df)
    finally:
        pass
    if not frames:
        return pd.DataFrame()
    all_df = pd.concat(frames, ignore_index=True)
    all_df = all_df.sort_values("timestamp").reset_index(drop=True)
    all_df["module_id"] = all_df["module_id"].astype("category")
    return all_df

# -----------------------------------------------------------
# 5. 페이지 제목 및 그래프 reload
# -----------------------------------------------------------
st.title("🔋 BMS 분석 자동화 대시보드")
REFRESH_INTERVAL_SEC = 3
st_autorefresh(interval=REFRESH_INTERVAL_SEC * 1000, key="data_refresh")

# -----------------------------------------------------------
# 6. DB에서 데이터 로딩
# -----------------------------------------------------------
if "bms_df" not in st.session_state:
    # 첫 번째 호출: 처음 70개 데이터 로드
    ## limit 0 offset 70
    bms_df = load_data_from_mysql(data_limit=0, increment=False, last_row=70)
    st.session_state.bms_df = bms_df
    st.session_state.data_limit = 70 
else:
    # 두 번째 호출부터 : 1개씩 추가 로딩
    ## limit 70 offset 70+1 ... offset 71+1...
    data_limit = st.session_state.data_limit
    bms_df = load_data_from_mysql(data_limit=data_limit, increment=True, last_row=1)
    st.session_state.bms_df = pd.concat([st.session_state.bms_df, bms_df], ignore_index=True)
    st.session_state.data_limit += 1 

# -----------------------------------------------------------
# 7. 생성 컬럼 (이상탐지, 온도, 효율 등)
# -----------------------------------------------------------
try:
    bms_df, anomalies_df = analyze_power_error(st.session_state.bms_df) 
    bms_df = calc_temp_rise_rate(bms_df)
    bms_df = calc_temp_imbalance(bms_df)
    bms_df = add_charge_efficiency(bms_df)
    bms_df['degradation_risk'] = bms_df.apply(predict_degradation, axis=1)
    abnormal_result = detect_abnormal_module(bms_df)
    result_him = []
    for item in abnormal_result:
        modified_item = {
            '모듈': item['module_id'],
            '평균 SOH': item['avg_soh'],
            '상태': item['status']
        }
        result_him.append(modified_item)

    st.session_state.bms_df = bms_df

except Exception as e:
    st.error(f"생성 컬럼 계산 중 오류가 발생했습니다: {e}")
    st.stop()

# -----------------------------------------------------------
# 8. 모듈 목록
# -----------------------------------------------------------
combined_sub = st.session_state.bms_df.copy()
if pd.api.types.is_categorical_dtype(bms_df["module_id"]):
    module_ids = bms_df["module_id"].cat.categories.tolist()
else:
    module_ids = sorted(bms_df["module_id"].unique().tolist())

# -----------------------------------------------------------
# 9. 모듈 데이터 분리 및 초기화
# -----------------------------------------------------------
module_dfs = {}
for module_id in module_ids:
    module_dfs[module_id] = bms_df[bms_df["module_id"] == module_id]

# -----------------------------------------------------------
# 10. 상태 초기화: 어떤 모듈이 선택되었는지, 이상치 로그 저장
# -----------------------------------------------------------
if 'selected_module_key' not in st.session_state:
    st.session_state.selected_module_key = "All Modules" # 기본값 설정
if 'anomaly_log' not in st.session_state:
    st.session_state.anomaly_log = []

# -----------------------------------------------------------
# 11. 메인 레이아웃: 왼쪽 컬럼 (모듈 선택, 모듈 상태) / 오른쪽 컬럼 (그래프)
# 비율을 1:4 (20%:80%)로 설정
# -----------------------------------------------------------
left_col, right_col = st.columns([1, 4]) 

# -----------------------------------------------------------
# 12. LEFT COLUMN (20%): 버튼, 상태 모니터링, 이상치 로그
# -----------------------------------------------------------

with left_col:
    st.markdown("<h2 style='text-align:center; color:#4B0082; margin-top:0;'>🔋 BMS Monitor</h2>", unsafe_allow_html=True)
    st.markdown("---")
    # ===============================
    # 12.1 - [모듈 선택 UI] - 버튼 방식
    # ===============================
    st.markdown("##### 🔍 모듈 선택")
    
    # 전체 모듈 버튼
    if st.button("All Modules", use_container_width=True, type='primary' if st.session_state.selected_module_key == "All Modules" else 'secondary', key="btn_all"):
        st.session_state.selected_module_key = "All Modules"
    
    # 모듈별 버튼
    for m in module_ids:
        label = f"{m}"
        if st.button(label, use_container_width=True, type='primary' if st.session_state.selected_module_key == label else 'secondary', key=f"btn_{m}"):
            st.session_state.selected_module_key = label
            
    # Outlier 버튼
    if st.button("🚨 Outlier", use_container_width=True, type='primary' if st.session_state.selected_module_key == "Outlier" else 'secondary', key="btn_outlier"):
        st.session_state.selected_module_key = "Outlier"

    # ===============================
    # 12.2 [상태 모니터링 박스] 및 이상치 로그 저장 로직
    # ===============================
    st.markdown("<br>", unsafe_allow_html=True)
    
    current_anomalies = []
    
    # 최신 타임스탬프의 데이터만 필터링
    if not bms_df.empty:
        latest_timestamp = bms_df["timestamp"].max()
        latest_rows = bms_df[bms_df["timestamp"] == latest_timestamp]
        
        for index, row in latest_rows.iterrows():
            m = row["module_id"]
            is_abnormal = detect_anomaly(row)  # 이상치 여부 판단
            
            if is_abnormal:
                # 이상치가 감지된 경우에만 로그 저장
                log_entry = {
                    "timestamp": row["timestamp"],
                    "module": m,
                    "temp": f"{row.get('cell_temperature_c', 0):.1f}",
                    "error": f"{row.get('power_error_kw', 0):.2f}",
                    "reason": "Threshold Exceeded"
                }
                
                # 중복 로그 방지 (가장 최근 타임스탬프가 이미 로그에 있는 경우 건너뜀)
                if not st.session_state.anomaly_log or st.session_state.anomaly_log[-1]["timestamp"] != row["timestamp"]:
                    st.session_state.anomaly_log.append(log_entry)
    # [상태 모니터링 박스] 및 이상치 로그 저장 로직
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    current_anomalies = []
    
    current_table_data = [] 

    # 각 모듈에 대한 상태 업데이트
    for m in module_ids:
        df_m = module_dfs[m]
        if not df_m.empty:  
            # 최신 데이터
            latest_row = df_m[df_m["timestamp"] == df_m["timestamp"].max()].iloc[0]
            is_abnormal = detect_anomaly(latest_row)

            
            if is_abnormal:
                current_anomalies.append(m)
                
                # 이상치 로그 저장
                log_entry = {
                    "timestamp": latest_row["timestamp"],
                    "module": m,
                    "temp": f"{latest_row.get('cell_temperature_c', 0):.1f}",
                    "error": f"{latest_row.get('power_error_kw', 0):.2f}",
                    "reason": "Threshold Exceeded"
                }
                # 중복 로그 방지
                if not st.session_state.anomaly_log or st.session_state.anomaly_log[-1]["timestamp"] != latest_row["timestamp"]:
                    st.session_state.anomaly_log.append(log_entry)

            # 실시간 상태 테이블 업데이트 데이터 수집
            temp = latest_row.get("cell_temperature_c", 0)
            status_text = "비정상" if is_abnormal else "정상"
            
            current_table_data.append({
                "모듈": m,
                "온도": f"{temp:.1f}",
                "상태": status_text
            })

    # 상태 테이블 표시
    if current_table_data:
        status_df = pd.DataFrame(result_him)
        st.markdown("#### 🔍 모듈 상태")
        st.dataframe(status_df, use_container_width=True, hide_index=True)

    # 이상치 로그 박스 표시 (이상치 탐지 후)
    if st.session_state.selected_module_key == "Outlier":
        status_msg = f"🚨 총 감지된 이상치: {len(st.session_state.anomaly_log)} 건"
        box_color = "#ffcccc"
    elif current_anomalies:
        # 경고 상태 (최신 데이터에서 이상치 발견)
        status_msg = f"⚠️ 경고 (Warning)<br><span style='font-size:0.8em'>이상 모듈: {', '.join(current_anomalies)}</span>"
        box_color = "#ffcccc"
    else:
        # 정상 상태
        status_msg = "✅ 정상 (Normal)"
        box_color = "#e6f2ff"
    # ===============================
    # 12.3 [상태 모니터링 박스 표시]
    # ===============================
    st.markdown(f"""
        <div class="status-box-inner" style="background-color: {box_color};">
            {status_msg}
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    

    
# -----------------------------------------------------------
# 13. RIGHT COLUMN (80%): 실시간 그래프 시각화
# -----------------------------------------------------------
with right_col:
    
    selected_key = st.session_state.selected_module_key

    if selected_key == "All Modules":
        # =========================
        # 13.1 All Modules 구역
        # =========================
        st.markdown("### 🌐 All Modules")


        ## 이상치 감지 로직 추가
        if not combined_sub.empty:
            combined_sub["anomaly_flag"] = combined_sub.apply(detect_anomaly, axis=1)
            if combined_sub["anomaly_flag"].any():
                st.error("🚨 이상치 감지! (All Modules)")

        ## 13.1 충/방전 효율 그래프
        if combined_sub.empty:
            st.info("표시할 데이터가 없습니다.")
        else:
            # --- Energy Input (All Modules) ---
            st.markdown("#### ⚡ Energy Input (All Modules)")

            if "energy_input_kwh" not in combined_sub.columns:
                st.error("energy_input_kwh 컬럼이 없습니다.")
            else:
                fig_energy_all = px.line(
                    combined_sub,
                    x="timestamp",
                    y="energy_input_kwh",
                    color="module_id",
                    template="plotly_white",
                )
                fig_energy_all.update_traces(mode="lines+markers")
                fig_energy_all.update_layout(
                    xaxis_title="시간",
                    yaxis_title="Energy Input (kWh)",
                    height=350,
                    legend_title="module_id",
                )

                st.plotly_chart(
                    fig_energy_all,
                    width='stretch',
                    key="all_energy_chart",
                )

            # --- 1행: Power / Current ---
            col_left, col_right = st.columns(2)

            ## 13.2 전류-전압 변화 그래프
            # Power Error (All Modules)
            with col_left:
                st.markdown("#### ⚡ Power Error (All Modules)")
                if "power_error_kw" not in combined_sub.columns:
                    st.error("power_error_kw 컬럼이 없습니다.")
                else:
                    fig_power_all = px.line(
                        combined_sub,
                        x="timestamp",
                        y="power_error_kw",
                        color="module_id",
                        template="plotly_white",
                    )
                    fig_power_all.update_traces(mode="lines+markers")
                    fig_power_all.update_layout(
                        xaxis_title="시간",
                        yaxis_title="power_error_kw [kW]",
                        height=350,
                    )
                    st.plotly_chart(
                        fig_power_all,
                        width='stretch',
                        key="all_power_chart",
                    )
            ## 13.3 충 방전 상태 그래프
            # Current Mode (All Modules)
            with col_right:
                st.markdown("#### 🔁 Current Mode (All Modules)")
                if "module_current_a" not in combined_sub.columns or "mode" not in combined_sub.columns:
                    st.error("module_current_a 또는 mode 컬럼이 없습니다.")
                else:
                    fig_curr_all = px.scatter(
                        combined_sub,
                        x="timestamp",
                        y="module_current_a",
                        color="mode",
                        symbol="module_id",
                        template="plotly_white",
                    )
                    fig_curr_all.update_layout(
                        xaxis_title="시간",
                        yaxis_title="module_current_a [A]",
                        height=350,
                    )
                    st.plotly_chart(
                        fig_curr_all,
                        width='stretch',
                        key="all_curr_chart",
                    )

            st.markdown("---")

            
            # --- 2행: Temperature Rise Rate + Module Temperature ---
            col_left, col_right = st.columns(2)

            ## 13.4 온도 상승 비율 그래프
            # Temperature Rise Rate (All Modules)
            with col_left:
                st.markdown("#### 🌡️ Temperature Rise Rate (All Modules)")
                if "temp_rise_rate" not in combined_sub.columns:
                    st.error("temp_rise_rate 컬럼이 없습니다.")
                else:
                    fig_temp_all = px.line(
                        combined_sub,
                        x="timestamp",
                        y="temp_rise_rate",
                        color="module_id",
                        template="plotly_white",
                    )
                    fig_temp_all.update_traces(mode="lines+markers")
                    fig_temp_all.update_layout(
                        xaxis_title="시간",
                        yaxis_title="온도 증가 속도 (°C/분)",
                        height=350,
                    )
                    fig_temp_all.add_hline(
                        y=2,
                        line_dash="dash",
                        line_color="red",
                        annotation_text="Threshold (2.0)",
                        annotation_position="top left",
                    )
                    st.plotly_chart(
                        fig_temp_all,
                        width='stretch',
                        key="all_temp_rise_chart",
                    )

            ## 13.5 온도 현재 상태 그래프
            # Module Temperatures (All Modules)
            with col_right:
                st.markdown("#### 🌡️ Module Temperatures (All Modules)")
                if "cell_temperature_c" not in combined_sub.columns:
                    st.error("cell_temperature_c 컬럼이 없습니다.")
                else:
                    fig_temp_modules = px.line(
                        combined_sub,
                        x="timestamp",
                        y="cell_temperature_c",
                        color="module_id",
                        template="plotly_white",
                    )
                    fig_temp_modules.update_traces(mode="lines")
                    fig_temp_modules.update_layout(
                        xaxis_title="시간",
                        yaxis_title="셀 온도 (°C)",
                        height=350,
                        legend_title="module_id",
                    )
                    st.plotly_chart(
                        fig_temp_modules,
                        width='stretch',
                        key="all_temp_modules_chart",
                    )

            st.markdown("---")

    elif selected_key == "Outlier":
        # =========================
        # 13. 2Outlier 섹션: Outlier 로그 시각화
        # =========================
        st.markdown("### 🚨 Outlier Data & Log")
        
        # -------------------------
        # [이상치 로그 테이블]
        # -------------------------
        st.markdown("##### 📜 이상치 발생 로그")
        log_df = pd.DataFrame(st.session_state.anomaly_log)
        if not log_df.empty:
            log_df["timestamp"] = log_df["timestamp"].dt.strftime("%Y-%m-%d %H:%M:%S")

            st.dataframe(log_df.tail(10).sort_values("timestamp", ascending=False), 
                          use_container_width=True, 
                          hide_index=True)
        else:
            st.info("기록된 이상치 로그가 없습니다.")
        

        # 이상치 데이터 필터링 (anomaly_flag가 True인 데이터만)
        sub_temp = bms_df.copy()
        sub_temp["anomaly_flag"] = sub_temp.apply(detect_anomaly, axis=1)
        sub_outlier = sub_temp[sub_temp["anomaly_flag"] == True]
        
        if sub_outlier.empty:
            st.info("현재 표시할 이상치 그래프 데이터가 없습니다.") 
        else:
            pass
        
    else:
        # =========================
        # 13.3 개별 모듈 섹션
        # =========================
        m = selected_key.replace("Module ", "")
        st.markdown(f"### 🔋 {selected_key}")
        df_to_display = module_dfs.get(m, pd.DataFrame())
        display_title_suffix = "(This Module)"
        anomaly_module_name = m

        if df_to_display.empty:
            st.info("표시할 데이터가 없습니다.")
        else:
            sub = df_to_display

            # anomaly_flag 계산
            sub["anomaly_flag"] = sub.apply(detect_anomaly, axis=1)

            # --- Energy Input ---
            st.markdown(f"#### ⚡ Energy Input {display_title_suffix}")
            if "energy_input_kwh" not in sub.columns:
                st.error("energy_input_kwh 컬럼이 없습니다")
            else:
                fig_energy = px.line(
                    sub,
                    x="timestamp",
                    y="energy_input_kwh",
                    color="module_id" if selected_key == "All Modules" else None,
                    template="plotly_white",
                )
                fig_energy.update_traces(mode="lines+markers")
                fig_energy.update_layout(
                    xaxis_title="시간",
                    yaxis_title="Energy Input (kWh)",
                    height=350,
                    legend_title="module_id" if selected_key == "All Modules" else None,
                )
                st.plotly_chart(fig_energy, use_container_width=True, key=f"{selected_key}_energy_chart")

            # --- 1행: Power / Current ---
            st.markdown("---")
            col_1_left, col_1_right = st.columns(2)

            # Power Error
            with col_1_left:
                st.markdown(f"#### ⚡ Power Error {display_title_suffix}")
                if "power_error_kw" not in sub.columns:
                    st.error("power_error_kw 컬럼이 없습니다.")
                else:
                    fig_power = px.line(
                        sub,
                        x="timestamp",
                        y="power_error_kw",
                        color="module_id" if selected_key == "All Modules" else None,
                        template="plotly_white",
                    )
                    fig_power.update_traces(mode="lines+markers")
                    fig_power.update_layout(
                        xaxis_title="시간",
                        yaxis_title="power_error_kw [kW]",
                        height=350,
                    )
                    st.plotly_chart(fig_power, use_container_width=True, key=f"{selected_key}_power_chart")

            # Current Mode
            with col_1_right:
                st.markdown(f"#### 🔁 Current Mode {display_title_suffix}")
                if "module_current_a" not in sub.columns or "mode" not in sub.columns:
                    st.error("module_current_a 또는 mode 컬럼이 없습니다.")
                else:
                    fig_curr = px.scatter(
                        sub,
                        x="timestamp",
                        y="module_current_a",
                        color="mode",
                        symbol="module_id" if selected_key == "All Modules" else None,
                        template="plotly_white",
                    )
                    fig_curr.update_layout(
                        xaxis_title="시간",
                        yaxis_title="module_current_a [A]",
                        height=350,
                    )
                    st.plotly_chart(fig_curr, use_container_width=True, key=f"{selected_key}_curr_chart")

            # --- 2행: Temperature Rise Rate + Module Temperature ---
            st.markdown("---")
            col_2_left, col_2_right = st.columns(2)

            # Temperature Rise Rate
            with col_2_left:
                st.markdown(f"#### 🌡️ Temperature Rise Rate {display_title_suffix}")
                if "temp_rise_rate" not in sub.columns:
                    st.error("temp_rise_rate 컬럼이 없습니다.")
                else:
                    fig_temp = px.line(
                        sub,
                        x="timestamp",
                        y="temp_rise_rate",
                        color="module_id" if selected_key == "All Modules" else None,
                        template="plotly_white",
                    )
                    fig_temp.update_traces(mode="lines+markers")
                    fig_temp.update_layout(
                        xaxis_title="시간",
                        yaxis_title="온도 증가 속도 (°C/분)",
                        height=350,
                    )
                    fig_temp.add_hline(
                        y=1,  # detect_anomaly 함수에서 사용된 임계값 1.0 반영
                        line_dash="dash",
                        line_color="red",
                        annotation_text="Threshold (1.0)",
                        annotation_position="top left",
                    )
                    st.plotly_chart(fig_temp, use_container_width=True, key=f"{selected_key}_temp_rise_chart")

            # Module Temperatures
            with col_2_right:
                st.markdown(f"#### 🌡️ Module Temperatures {display_title_suffix}")
                if "cell_temperature_c" not in sub.columns:
                    st.error("cell_temperature_c 컬럼이 없습니다.")
                else:
                    fig_temp_modules = px.line(
                        sub,
                        x="timestamp",
                        y="cell_temperature_c",
                        color="module_id" if selected_key == "All Modules" else None,
                        template="plotly_white",
                    )
                    fig_temp_modules.update_traces(mode="lines")
                    fig_temp_modules.update_layout(
                        xaxis_title="시간",
                        yaxis_title="셀 온도 (°C)",
                        height=350,
                        legend_title="module_id" if selected_key == "All Modules" else None,
                    )
                    st.plotly_chart(fig_temp_modules, use_container_width=True, key=f"{selected_key}_temp_modules_chart")

            st.markdown("---")

