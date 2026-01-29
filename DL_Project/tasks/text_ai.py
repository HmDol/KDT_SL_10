# tasks/text_ai.py
import torch
import torch.nn as nn
from transformers import BertModel, BertTokenizer

# =========================
# 환경 설정 (노트북 기준)
# =========================
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

PRETRAINED = "skt/kobert-base-v1"
MAX_LEN = 254                 # 노트북에서 사용한 값
NUM_LABELS = 2                # 0=Human, 1=AI

WEIGHT_PATH = "weights/text_kobert.pt"   # best_head_only.pt 복사해서 사용


# =========================
# 1) 모델 정의 (노트북 그대로)
# =========================
class KoBERTLinearHeadClassifier(nn.Module):
    def __init__(self):
        super().__init__()

        self.bert = BertModel.from_pretrained(PRETRAINED)

        # backbone freeze
        for p in self.bert.parameters():
            p.requires_grad = False

        self.classifier = nn.Sequential(
            nn.Linear(768, 256),
            nn.GELU(),
            nn.Dropout(0.3),
            nn.Linear(256, NUM_LABELS)
        )

    def forward(self, input_ids, attention_mask):
        outputs = self.bert(
            input_ids=input_ids,
            attention_mask=attention_mask
        )
        cls = outputs.last_hidden_state[:, 0, :]  # [CLS]
        logits = self.classifier(cls)
        return logits


# =========================
# 2) 토크나이저 / 모델 로딩 (🔥 import 시 1회)
# =========================
tokenizer = BertTokenizer.from_pretrained(PRETRAINED)

model = KoBERTLinearHeadClassifier().to(DEVICE)
model.load_state_dict(
    torch.load(WEIGHT_PATH, map_location=DEVICE)
)
model.eval()


# =========================
# 3) 전처리 (노트북 Dataset 로직)
# =========================
def preprocess(text: str):
    """
    raw text → KoBERT input tensor
    """
    enc = tokenizer(
        text,
        truncation=True,
        padding="max_length",
        max_length=MAX_LEN,
        return_tensors="pt"
    )

    return {
        "input_ids": enc["input_ids"].to(DEVICE),
        "attention_mask": enc["attention_mask"].to(DEVICE)
    }


# =========================
# 4) GUI에서 호출하는 함수 (⭐ 핵심)
# =========================
@torch.no_grad()
def predict(text: str):
    """
    Returns:
        {
          label: int,          # 0=Human, 1=AI
          confidence: float,
          detail: dict
        }
    """
    if text is None or not str(text).strip():
        return {
            "label": -1,
            "confidence": 0.0,
            "detail": {"error": "Empty input"}
        }

    inputs = preprocess(text)
    logits = model(**inputs)
    probs = torch.softmax(logits, dim=1).squeeze(0)

    pred_label = int(torch.argmax(probs))
    confidence = float(probs[pred_label])

    return {
        "label": pred_label,
        "confidence": confidence,
        "detail": {
            "human_prob": float(probs[0]),
            "ai_prob": float(probs[1])
        }
    }
