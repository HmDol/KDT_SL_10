import gradio as gr
from inference import predict_all
import time, random

# =============================
# 기존: 얼굴 분석
# =============================
def predict_ui(image):
    return predict_all(image)

# =============================
# 추가: 트리 애니메이션(텍스트 스트리밍)
# =============================
TREE_W, TREE_H = 360, 26
flakes = ['*', '.', '❄', '•']

tree = [
    "                    ★",
    "                   ***",
    "                  *****",
    "                 *******",
    "                *********",
    "               ***********",
    "              *************",
    "             ***************",
    "            *****************",
    "           *******************",
    "          *********************",
    "         ***********************",
    "        *************************",
    "       ***************************",
    "      *****************************",
    "     *******************************",
    "    *********************************",
    "   ***********************************",
    "  *************************************",
    "                        |||",
    "                        |||",
    "                        |||",
    "                        |||",
    "                        |||",
]
TREE_BASE_Y = TREE_H - len(tree) - 2

def make_tree_state():
    return {"snow": [], "ground": [1]*TREE_W, "star_pulse": 0}

def create_flake():
    return {
        "x": random.randint(0, TREE_W - 1),
        "y": 0,
        "char": random.choice(flakes),
        "speed": random.choice([1, 1, 2]),
        "wind": random.choice([-1, 0, 1]),
    }

def maybe_add_flake(state):
    if random.random() < 0.5:
        state["snow"].append(create_flake())

def update_snow(state):
    snow = state["snow"]
    ground = state["ground"]
    for f in list(snow):
        f["y"] += f["speed"]
        f["x"] = (f["x"] + f["wind"]) % TREE_W

        if f["y"] >= TREE_H - ground[f["x"]]:
            snow.remove(f)
            ground[f["x"]] = min(ground[f["x"]] + 1, TREE_H - 1)

TREE_MAX_LEN = max(len(line) for line in tree)

def draw_tree(buf, state):
    start_y = TREE_BASE_Y
    start_x = (TREE_W // 2) - (TREE_MAX_LEN // 2)

    for i, line in enumerate(tree):
        for j, ch in enumerate(line):
            y, x = start_y + i, start_x + j
            if 0 <= y < TREE_H and 0 <= x < TREE_W:
                if i == 0 and ch == "*":
                    buf[y][x] = "★"
                else:
                    buf[y][x] = ch

def draw_snow(buf, state):
    for f in state["snow"]:
        x, y = f["x"], f["y"]
        if 0 <= y < TREE_H and 0 <= x < TREE_W:
            buf[y][x] = f["char"]

def render_frame(state):
    buf = [[" "]*TREE_W for _ in range(TREE_H)]
    draw_tree(buf, state)
    draw_snow(buf, state)
    return "\n".join("".join(row) for row in buf)

def tree_stream(state):
    # generator: 프레임을 계속 yield
    while True:
        yield render_frame(state)
        maybe_add_flake(state)
        update_snow(state)
        state["star_pulse"] += 1
        time.sleep(0.1)

# =============================
# UI
# =============================
with gr.Blocks(title="Face Analysis ML Dashboard") as demo:
    gr.Markdown(
        """
        <br><br>
        <h3>성별 · 인종 · 연령 · 감정 예측 모델</h3>
        <br>
        """
    )

    with gr.Row():
        with gr.Column(scale=1):
            image_input = gr.Image(label="얼굴 사진 업로드", type="numpy")
            submit_btn = gr.Button("분석 실행")
            crop_out = gr.Image(label="검출된 얼굴(크롭)", type="numpy", interactive=False)

        with gr.Column(scale=1):
            gender_out = gr.Textbox(label="성별", interactive=False)
            ethnicity_out = gr.Textbox(label="인종", interactive=False)
            age_out = gr.Textbox(label="연령", interactive=False)
            emotion_out = gr.Textbox(label="감정", interactive=False)

            gr.Markdown("### 상세 결과")
            with gr.Tabs():
                with gr.Tab("성별"):
                    gender_detail = gr.Label(label="성별 확률(%)")
                with gr.Tab("인종"):
                    ethnicity_detail = gr.Label(label="인종 확률(%)")
                with gr.Tab("연령"):
                    age_detail = gr.Label(label="연령 확률(%)")
                with gr.Tab("감정"):
                    emotion_detail = gr.Label(label="감정 확률(%)")

    submit_btn.click(
        fn=predict_ui,
        inputs=image_input,
        outputs=[
            gender_out, ethnicity_out, age_out, emotion_out, crop_out,
            gender_detail, ethnicity_detail, age_detail, emotion_detail
        ],
    )

    # =============================
    # 아래에 "트리 애니메이션" 섹션 추가
    # =============================
    gr.Markdown("---")
    gr.Markdown("## 🎄 크리스마스 트리 (눈 애니메이션)")

    with gr.Row():
        with gr.Column(scale=1):
            tree_start = gr.Button("트리 시작")
            tree_box = gr.Textbox(
                label="Tree Scene",
                lines=TREE_H,
                interactive=False
            )
            tree_state = gr.State(make_tree_state())

    # Start 누르면 스트리밍 시작
    tree_start.click(
        fn=tree_stream,
        inputs=tree_state,
        outputs=tree_box
    )

demo.launch()
