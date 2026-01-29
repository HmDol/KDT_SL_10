# tasks/deepfake_ai.py
import torch
import torch.nn as nn
import numpy as np
import cv2
import joblib
from PIL import Image
from pathlib import Path

# =========================
# 환경 설정 (노트북 기준)
# =========================
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

IMG_SIZE = 128
NUM_CLASSES = 2

WEIGHT_PATH = Path("weights/fake_model.pth")
PREPROCESS_PATH = Path("weights/fake_preprocess_params.joblib")


# =========================
# 1) 모델 정의 (노트북 그대로)
# =========================
class DeepFakeModel(nn.Module):
    def __init__(self, in_dim=49152, num_classes=2):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(),
            nn.Dropout(0.3),

            nn.Linear(1024, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.Dropout(0.2),

            nn.Linear(512, 128),
            nn.BatchNorm1d(128),
            nn.ReLU(),

            nn.Linear(128, 32),
            nn.BatchNorm1d(32),
            nn.ReLU(),
            nn.Dropout(0.1),

            nn.Linear(32, num_classes),
        )

    def forward(self, x):
        return self.net(x)


# =========================
# 2) 전처리 파라미터 로딩 (mean / std)
# =========================
if not PREPROCESS_PATH.exists():
    raise FileNotFoundError(
        f"[deepfake_ai] 전처리 파라미터 파일 없음: {PREPROCESS_PATH}"
    )

params = joblib.load(PREPROCESS_PATH)
mean = np.array(params["mean"], dtype=np.float32)  # shape (3,)
std  = np.array(params["std"], dtype=np.float32)


# =========================
# 3) 모델 로딩 (🔥 import 시 1회)
# =========================
model = DeepFakeModel().to(DEVICE)

if not WEIGHT_PATH.exists():
    raise FileNotFoundError(
        f"[deepfake_ai] 모델 weight 파일 없음: {WEIGHT_PATH}"
    )

model.load_state_dict(torch.load(WEIGHT_PATH, map_location=DEVICE))
model.eval()


# =========================
# 4) 전처리 (노트북 로직 그대로)
# =========================
def preprocess(image: Image.Image):
    """
    PIL.Image → (1, 49152) Tensor
    """
    # PIL → numpy (RGB)
    img = np.array(image)

    # RGB → BGR (cv2.imread와 동일한 분포 맞추기)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # resize
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE), interpolation=cv2.INTER_AREA)

    # float / normalize
    x = img.astype(np.float32) / 255.0
    x = (x - mean) / std

    # flatten
    x = x.reshape(-1)

    return torch.tensor(x, dtype=torch.float32).unsqueeze(0).to(DEVICE)


# =========================
# 5) GUI에서 호출하는 함수 (⭐ 핵심)
# =========================
@torch.no_grad()
def predict(image: Image.Image):
    """
    Returns:
        {
          label: int,          # 0=Real, 1=Fake
          confidence: float,
          detail: dict
        }
    """
    if image is None:
        return {
            "label": -1,
            "confidence": 0.0,
            "detail": {"error": "No image input"}
        }

    x = preprocess(image)
    logits = model(x)
    probs = torch.softmax(logits, dim=1).squeeze(0)

    pred_label = int(torch.argmax(probs))
    confidence = float(probs[pred_label])

    return {
        "label": pred_label,   # 0=Real, 1=Fake
        "confidence": confidence,
        "detail": {
            "real_prob": float(probs[0]),
            "fake_prob": float(probs[1])
        }
    }
