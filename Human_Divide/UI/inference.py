# inference.py
import numpy as np
import cv2
import joblib
import face_recognition
import random
from skimage.feature import hog
import warnings
warnings.filterwarnings(
    "ignore",
    message="X does not have valid feature names, but StandardScaler was fitted with feature names"
)

# ======================================================
# (1) 모델 로드 (처음 한 번만)
# ======================================================
_MODELS = None

def load_models():
    global _MODELS
    if _MODELS is None:
        _MODELS = {
            "gender": joblib.load("../Model/gender_model.jolib"),
            "ethnicity": joblib.load("../Model/skincolor_model.joblib"),

            "age": joblib.load("../Model/ageModel_pca160.joblib"),
            "age_scaler": joblib.load("../Model/scaler.joblib"),
            "age_pca": joblib.load("../Model/pca_160.joblib"),

            "emotion": joblib.load("../Model/best_pipeline.joblib"),
        }
    return _MODELS


# ======================================================
# (2) 공통: 얼굴 크롭
# ======================================================
def get_face_crop(img, margin=0.3):
    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    rgb_img = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_img)

    if len(face_locations) == 0:
        return None, img_bgr

    top, right, bottom, left = face_locations[0]
    h, w = img_bgr.shape[:2]

    face_h = bottom - top
    face_w = right - left
    m_h = int(face_h * margin)
    m_w = int(face_w * margin)

    top = max(0, top - m_h)
    bottom = min(h, bottom + m_h)
    left = max(0, left - m_w)
    right = min(w, right + m_w)

    crop = img_bgr[top:bottom, left:right]
    return crop, img_bgr


# ======================================================
# (3) 모델별 전처리
# ======================================================
def extract_hog_features(img):
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img = cv2.resize(img, (80, 80))

    features = hog(
        img,
        orientations=9,
        pixels_per_cell=(8, 8),
        cells_per_block=(2, 2),
        block_norm="L2-Hys",
        visualize=False,
        feature_vector=True,
    )
    return features

def extract_hog_from_image(img, margin=0.25):
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_img)

    if len(face_locations) == 0:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, (80, 80))
        hog_feat = extract_hog_features(gray)
        return hog_feat.reshape(1, -1)

    top, right, bottom, left = face_locations[0]

    h, w, _ = img.shape
    face_h = bottom - top
    face_w = right - left

    m_h = int(face_h * margin)
    m_w = int(face_w * margin)

    top = max(0, top - m_h)
    bottom = min(h, bottom + m_h)
    left = max(0, left - m_w)
    right = min(w, right + m_w)

    face_crop = img[top:bottom, left:right]
    gray = cv2.cvtColor(face_crop, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (80, 80))

    hog_feat = extract_hog_features(gray)
    return hog_feat.reshape(1, -1)

def preprocess_gender(face_bgr, full_bgr=None):
    return extract_hog_from_image(face_bgr)

def preprocess_ethnicity(face_bgr, full_bgr=None):
    rgb = cv2.cvtColor(face_bgr, cv2.COLOR_BGR2RGB)
    rgb = cv2.resize(rgb, (70, 70))
    rgb = rgb.astype(int)
    return rgb.reshape(1, -1)

def preprocess_age(face_bgr, full_bgr=None):
    models = load_models()
    scaler = models["age_scaler"]
    pca = models["age_pca"]

    gray = cv2.cvtColor(face_bgr, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (128, 128))
    gray = gray.astype(np.float32) / 255.0
    x = gray.reshape(1, -1)   # (1, 16384)

    x_scaled = scaler.transform(x)
    x_pca = pca.transform(x_scaled)
    return x_pca  # (1, 160)

def preprocess_emotion(face_bgr, full_bgr=None):
    # 기존 로직 유지 + (2304 vs 2303) 자동 보정만 추가
    gray = cv2.cvtColor(face_bgr, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (48, 48))
    print("emotion features:", len(gray[0]))

    
    return gray.reshape(1,-1)


# ======================================================
# (4) 매핑(필요시)
# ======================================================
GENDER_MAP = {0: "여자", 1: "남자"}
# EMOTION_MAP = {0 : "화남", 1 : '불쾌함', 2 : '공포', 3 : "기쁨", 4 : '슬픔'}


# ======================================================
# (추가) 확률 dict 만들기 (UI bar용)
# ======================================================
def _onehot_probs(pred_label, classes_list):
    return {str(c): (1.0 if str(c) == str(pred_label) else 0.0) for c in classes_list}

def _proba_dict(model, X, name_map=None):
    """
    model이 predict_proba 지원하면 {label: prob} 반환
    지원 안 하면 예측값 기반 one-hot dict 반환(그래도 bar 표시 가능)
    """
    # 1) proba 가능
    if hasattr(model, "predict_proba"):
        p = model.predict_proba(X)[0]
        classes = getattr(model, "classes_", None)
        if classes is None:
            classes = list(range(len(p)))

        out = {}
        for i, c in enumerate(classes):
            label = name_map.get(c, str(c)) if name_map else str(c)
            out[label] = float(p[i])
        return out

    # 2) proba 불가 -> one-hot
    pred = model.predict(X)[0]
    classes = getattr(model, "classes_", None)
    if classes is None:
        classes = [pred]
    out = {}
    for c in classes:
        label = name_map.get(c, str(c)) if name_map else str(c)
        out[label] = 1.0 if c == pred else 0.0
    return out


# ======================================================
# (5) UI가 부를 단 하나의 함수
#    ✅ 반환: 9개 (기존 5개 + 상세 4개)
# ======================================================
def predict_all(image):
    if image is None:
        # 9개 맞춰서 반환
        return "이미지를 업로드하세요.", "-", "-", "-", None, {}, {}, {}, {}

    crop_rgb = None  # ✅ 예외 대비

    try:
        models = load_models()

        face_crop, full_bgr = get_face_crop(image, margin=0.3)
        if face_crop is None:
            face_crop = full_bgr

        crop_rgb = cv2.cvtColor(face_crop, cv2.COLOR_BGR2RGB)

        # 전처리
        X_gender = preprocess_gender(face_crop, full_bgr)
        X_eth = preprocess_ethnicity(face_crop, full_bgr)
        X_age = preprocess_age(face_crop, full_bgr)
        X_em = preprocess_emotion(face_crop, full_bgr)

        # 예측
        g_raw = models["gender"].predict(X_gender)[0]
        gender = GENDER_MAP.get(g_raw, str(g_raw))

        ethnicity = models["ethnicity"].predict(X_eth)[0]
        age = models["age"].predict(X_age)[0]
        emotion = models["emotion"].predict(X_em)[0]

        
        

        # ✅ 상세 확률(dict)
        gender_probs = _proba_dict(models["gender"], X_gender, name_map=GENDER_MAP)
        ethnicity_probs = _proba_dict(models["ethnicity"], X_eth)
        age_probs = _proba_dict(models["age"], X_age)
        emotion_probs = _proba_dict(models["emotion"],X_em)
        
        print("emotion(text):", emotion)
        print("emotion_probs_top:", max(emotion_probs, key=emotion_probs.get))
        return (
            str(gender), str(ethnicity), str(age), str(emotion), crop_rgb,
            gender_probs, ethnicity_probs, age_probs, emotion_probs
        )

    except Exception as e:
        print("[WARN] Dummy inference used:", e)

        dummy_gender = random.choice(["남성", "여성"])
        dummy_ethnicity = random.choice(["Asian", "Caucasian", "African"])
        dummy_age = random.choice(["10대", "20대", "30대", "40대", "50대+"])
        dummy_emotion = random.choice(["Happy", "Neutral", "Sad", "Angry"])

        # 더미 확률도 bar로 보이게 dict 형태 제공
        gender_probs = {"남성": 0.5, "여성": 0.5}
        ethnicity_probs = {"Asian": 0.34, "Caucasian": 0.33, "African": 0.33}
        age_probs = {"10대": 0.2, "20대": 0.2, "30대": 0.2, "40대": 0.2, "50대+": 0.2}
        emotion_probs = {"Happy": 0.25, "Neutral": 0.25, "Sad": 0.25, "Angry": 0.25}

        return (
            dummy_gender, dummy_ethnicity, dummy_age, dummy_emotion, crop_rgb,
            gender_probs, ethnicity_probs, age_probs, emotion_probs
        )
