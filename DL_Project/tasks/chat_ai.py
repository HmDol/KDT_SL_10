# tasks/chat_ai.py
import json
import re
import torch
import torch.nn as nn
import torch.nn.functional as F
from konlpy.tag import Okt
from pathlib import Path

import pickle

# =========================
# 환경 설정 (chat.ipynb 기준)
# =========================
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

MAX_LEN = 50                 # chat.ipynb에서 사용
EMBEDDING_DIM = 100
HIDDEN_DIM = 64
NUM_LABELS = 1               # sigmoid 이진분류
THRESHOLD = 0.5

VOCAB_PATH = Path("weights/chat_vocab.pkl")
WEIGHT_PATH = Path("weights/chat_weights.pt")

MAX_TURNS = 6                # history 너무 길어지는 거 방지


# =========================
# 1) 모델 정의 (chat.ipynb 그대로)
# =========================
class TextClassifier(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, dropout=0.3):
        super().__init__()

        self.embedding = nn.Embedding(
            vocab_size, embedding_dim, padding_idx=0
        )
        self.lstm = nn.LSTM(
            embedding_dim, hidden_dim, batch_first=True
        )

        self.fc1 = nn.Linear(hidden_dim, 32)
        self.fc2 = nn.Linear(32, 16)
        self.dropout = nn.Dropout(dropout)
        self.out = nn.Linear(16, 1)

    def forward(self, x):
        # x: (B, T)
        x = self.embedding(x)
        _, (hidden, _) = self.lstm(x)

        x = hidden[-1]
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = F.relu(self.fc2(x))
        return torch.sigmoid(self.out(x))  # (B, 1)


# =========================
# 2) 리소스 로딩 (🔥 import 시 1회)
# =========================
okt = Okt()

if not VOCAB_PATH.exists():
    raise FileNotFoundError("chat_vocab.pkl 파일이 없습니다.")

with open(VOCAB_PATH, "rb") as f:
    word_to_index = pickle.load(f)

# value가 str로 들어왔을 수도 있으니 안전하게 캐스팅
word_to_index = {k: int(v) for k, v in word_to_index.items()}
vocab_size = len(word_to_index)

model = TextClassifier(
    vocab_size,
    EMBEDDING_DIM,
    HIDDEN_DIM
).to(DEVICE)

if not WEIGHT_PATH.exists():
    raise FileNotFoundError(
        f"[chat_ai] weight 파일 없음: {WEIGHT_PATH}"
    )

model.load_state_dict(torch.load(WEIGHT_PATH, map_location=DEVICE))
model.eval()


# =========================
# 3) 전처리 (chat.ipynb 로직)
# =========================
def _clean_text(text: str) -> str:
    text = re.sub(r"[^가-힣a-zA-Z0-9\s]", "", str(text))
    return text.strip()


def _build_chat_text(message: str, history):
    """
    chat.ipynb는 '단문 문장' 분포라
    → history 전부 다 쓰면 오히려 성능 깨짐
    → user 발화만 최근 N개 사용
    """
    history = history or []
    history = history[-MAX_TURNS:]

    parts = []
    for u, _ in history:
        if u:
            parts.append(str(u))

    parts.append(str(message))
    return " ".join(parts)


def _text_to_tensor(text: str):
    tokens = okt.morphs(text, stem=True)

    seq = [word_to_index.get(w, 1) for w in tokens]  # 1 = <UNK>

    if len(seq) < MAX_LEN:
        seq += [0] * (MAX_LEN - len(seq))
    else:
        seq = seq[:MAX_LEN]

    return torch.tensor(
        [seq], dtype=torch.long, device=DEVICE
    )  # (1, 50)


# =========================
# 4) GUI에서 호출하는 함수 (⭐ 핵심)
# =========================
@torch.no_grad()
def predict(message: str, history=None):
    """
    Returns:
        {
          label: 0(HUMAN) / 1(AI)
          confidence: float
          detail: dict
        }
    """
    if message is None or not str(message).strip():
        return {
            "label": -1,
            "confidence": 0.0,
            "detail": {"error": "Empty input"}
        }

    merged_text = _build_chat_text(message, history)
    merged_text = _clean_text(merged_text)

    if not merged_text:
        return {
            "label": -1,
            "confidence": 0.0,
            "detail": {"error": "Empty after cleaning"}
        }

    x = _text_to_tensor(merged_text)
    score = float(model(x).item())  # sigmoid → P(AI)

    pred_label = 1 if score >= THRESHOLD else 0
    confidence = score if pred_label == 1 else (1.0 - score)

    return {
        "label": pred_label,     # 0=HUMAN, 1=AI
        "confidence": confidence,
        "detail": {
            "human_prob": 1.0 - score,
            "ai_prob": score
        }
    }
