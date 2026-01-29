# tasks/image_ai.py
import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image

# =========================
# 환경 설정 (photo.ipynb 기준)
# =========================
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

IMG_SIZE = 32
NUM_LABELS = 1   # sigmoid 이진 분류
THRESHOLD = 0.5

WEIGHT_PATH = "weights/img_weights.pt"   # photo.ipynb에서 저장한 weight


# =========================
# 1) 모델 정의 (photo.ipynb imgModel 그대로)
# =========================
class ImgModel(nn.Module):
    def __init__(self, img_h=32, img_w=32, channels=3,
                 hidden1=512, hidden2=128, dropout_p=0.3):
        super().__init__()

        in_dim = channels * img_h * img_w

        self.net = nn.Sequential(
            nn.Flatten(),
            nn.Linear(in_dim, hidden1),
            nn.ReLU(),
            nn.Dropout(dropout_p),

            nn.Linear(hidden1, hidden2),
            nn.ReLU(),
            nn.Dropout(dropout_p),

            nn.Linear(hidden2, 1)  # BCEWithLogitsLoss용
        )

    def forward(self, x):
        return self.net(x)


# =========================
# 2) 전처리 (photo.ipynb inference_tfms)
# =========================
transform = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor()  # 0~1
])


def preprocess(image: Image.Image):
    """
    PIL.Image → Tensor [1, 3, 32, 32]
    """
    if image.mode != "RGB":
        image = image.convert("RGB")

    x = transform(image)
    return x.unsqueeze(0).to(DEVICE)


# =========================
# 3) 모델 로딩 (🔥 import 시 1회)
# =========================
model = ImgModel().to(DEVICE)
model.load_state_dict(torch.load(WEIGHT_PATH, map_location=DEVICE))
model.eval()


# =========================
# 4) GUI에서 호출하는 함수 (⭐ 핵심)
# =========================
@torch.no_grad()
def predict(image: Image.Image):
    """
    Args:
        image (PIL.Image): Gradio Image 입력

    Returns:
        dict:
            {
              "label": int,          # 0=FAKE, 1=REAL
              "confidence": float,   # 예측 클래스 확률
              "detail": dict
            }
    """
    if image is None:
        return {
            "label": -1,
            "confidence": 0.0,
            "detail": {"error": "No image input"}
        }

    x = preprocess(image)
    logit = model(x)
    prob = torch.sigmoid(logit).item()   # P(REAL)

    # photo.ipynb 기준: threshold=0.5
    pred_label = 1 if prob >= THRESHOLD else 0

    confidence = prob if pred_label == 1 else (1.0 - prob)

    return {
        "label": pred_label,   # 0=FAKE, 1=REAL
        "confidence": confidence,
        "detail": {
            "real_prob": prob,
            "fake_prob": 1.0 - prob
        }
    }
