import time
import pymysql

# DB 연결
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='mysql',
    database='projectdb',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = conn.cursor()

# origin → module 매핑
table_mapping = {
    "origina": "moduleA_tbl",
    "originb": "moduleB_tbl",
    "originc": "moduleC_tbl",
    "origind": "moduleD_tbl",
    "origine": "moduleE_tbl"
}

# INSERT 템플릿
insert_sql = """
INSERT INTO {table} (
    `timestamp`,
    `module_id`,
    `cell_voltage_v`,
    `cell_temperature_c`,
    `module_current_a`,
    `module_power_kw`,
    `converter_command_pct`,
    `soc_pct`,
    `soh_pct`,
    `anomaly_score_pct`,
    `diagnostic_flag`,+++++++                                                                   
    `latency_ms`
)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

print(" Streaming 시작 (단위 초마다 1줄씩 처리)...\nCtrl + C 로 중지 가능.\n")
flag = True

try:
    while flag:

        for origin_table, module_table in table_mapping.items():

            # module 테이블 현재 개수 확인 → 다음 insert row 번호 결정
            cursor.execute(f"SELECT COUNT(*) AS cnt FROM {module_table}")
            inserted_count = cursor.fetchone()['cnt']

            # origin 테이블에서 다음 행 가져오기 (index = inserted_count)
            cursor.execute(
                f"SELECT * FROM {origin_table} ORDER BY timestamp ASC LIMIT 1 OFFSET {inserted_count}"
            )
            row = cursor.fetchone()


            # origin보다 module 데이터가 더 많으면 skip
            if row is None:
                print(f" {module_table}: 모든 데이터 입력 완료!")
                flag = False
                continue

            # INSERT 수행
            values = (
                row['timestamp'], row['module_id'], row['cell_voltage_v'], row['cell_temperature_c'],
                row['module_current_a'], row['module_power_kw'], row['converter_command_pct'],
                row['soc_pct'], row['soh_pct'], row['anomaly_score_pct'],
                row['diagnostic_flag'], row['latency_ms']
            )

            cursor.execute(insert_sql.format(table=module_table), values)
            conn.commit()

            print(f" {module_table}: {inserted_count+1}번째 데이터 INSERT 성공 → timestamp: {row['timestamp']}")

        # -------- 2초 대기 --------
        time.sleep(2)

except KeyboardInterrupt:
    print("\n 스트리밍 중단됨.")

finally:
    cursor.close()
    conn.close()
    print("🔌 DB 연결 종료.")
