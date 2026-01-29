## ========================================================
## Filename     : util_func.py
## Description  : 인공신공망 학습/검증 및 출력 관련 함수들
## ========================================================
import torch
import matplotlib.pyplot as plt
from torchmetrics.regression import *
from torchmetrics.classification import *

## ========================================================
## 함수이름 : train_one_epoch
## 반환결과 : 손실, 정확도
## ========================================================
def train_one_epoch(model, loader, loss_fn, optim, device):
    ## 모델 동작 모드 설정 : 반드시 학습 전에 서정
    model.train()

    ## 1에포크 후 학습 결과 저장용
    total_loss, correct, total = 0.0, 0, 0

    ## 배치크기만큼 학습 진행
    for x, y in loader:
        ## 피쳐, 타겟 추출 후 위치 설정 
        ## -> GPU 메모리로 복사(이동)
        x, y = x.to(device), y.to(device)

        ## 순전파 
        logits = model(x)
        optim.zero_grad()
        loss = loss_fn(logits, y)

        ## 역전파
        loss.backward()
        optim.step()

        ## 학습 결과 계산 밑 저장 
        total_loss += loss.item() * x.size(0)
        pred = logits.argmax(dim=1)
        correct += (pred == y).sum().item()
        total += x.size(0)

    return total_loss / total, correct / total


## ========================================================
## 함수이름 : evaluate
## 함수기능 : 검증/테스트 시 사용
##           역전파 진행 하지 않음!!!
## 반환결과 : 손실, 정확도
## ========================================================
@torch.no_grad()
def evaluate(model, loader, loss_fn, device):
    ## 모델 동작 모드 => 학습에 필수적인 기능들 비활성화
    model.eval()

    ## 검증 시 결과 저장 변수들
    total_loss, correct, total = 0.0, 0, 0

    ## 검증/테스트용 배치크기만큼 로딩 후 예측 진행
    for x, y in loader:
        ## 피쳐, 타겟 추출 후 위치 설정 
        ## -> GPU 메모리로 복사(이동)
        x, y = x.to(device), y.to(device)

        ## 순전파
        logits = model(x)
        loss = loss_fn(logits, y)

        ## 예측 결과 저장 
        total_loss += loss.item() * x.size(0)
        pred        = logits.argmax(dim=1)
        correct    += (pred == y).sum().item()
        total      += x.size(0)

    return total_loss / total, correct / total



## ========================================================
## 함수이름 : train_one_epoch_reg
## 함수기능 : 학습 진행
## 반환결과 : avg_loss, r2_value, mae_value
## ========================================================
def train_one_epoch_reg(model, loader, loss_fn, optim, device):
    ## 학습모드
    model.train()

    ## 성능지표 인스턴스
    mae  = MeanAbsoluteError().to(device)
    rmse = MeanSquaredError(squared=False).to(device)  # RMSE
    r2   = R2Score().to(device)                        # 단일 출력 회귀 기준

    ## 저장 변수들 초기화
    sum_loss, total_samples = 0.0, 0

    ## 계산 및 검증 진행 
    for x, y in loader:
        ## 배치크기만큼 데이터 로딩
        x, y = x.to(device), y.to(device)

        ## 예측 및 shape 맞추기
        pred = model(x).view_as(y)    

        ## 손실 계산 
        loss = loss_fn(pred, y)

        ## 역전파
        optim.zero_grad()
        loss.backward()
        optim.step()

        ## 손실값 가중 누적 저장
        bs = x.size(0)
        sum_loss += loss.item() * bs
        total_samples += bs

        ## metric 누적 (학습 중이므로 detach 권장)
        p = pred.detach()

        ## 성능지표값 누적 
        mae.update(p, y)
        rmse.update(p, y)
        r2.update(p, y)

    ## 에포크 단위의 평균 loss, R2 저장 
    avg_loss   = sum_loss / max(total_samples, 1)
    mae_value  = mae.compute().item()
    r2_value   = r2.compute().item()

    return avg_loss, r2_value, mae_value


## ========================================================
## 함수이름 : evaluate_reg
## 함수기능 : 검증/테스트 시 사용
##           역전파 진행 하지 않음!!!
## 반환결과 : avg_loss, r2_value, mae_value
## ========================================================

@torch.no_grad()
def evaluate_reg(model, loader, loss_fn, device):
    ## 검증모드
    model.eval()

    ## 성능지표 인스턴스
    r2  = R2Score().to(device)
    mse = MeanSquaredError().to(device)

    ## 저장 변수들 초기화
    total_loss, total = 0.0, 0

    ## 예측 진행 
    for x, y in loader:
        ## 배치크기만큼 데이터 로딩
        x, y = x.to(device), y.to(device)

        ## 예측
        pred = model(x)

        ## 예측과 정답 shape 맞추기
        pred = pred.view_as(y)

        ## 손실 계산 
        loss = loss_fn(pred, y)

        ## 손실값 가중 누적 저장
        bs   = x.size(0)
        total_loss += loss.item() * bs
        total += bs

        ## 성능지표값 누적 
        r2.update(pred, y)
        mse.update(pred, y)

    ## 에포크 단위의 평균 loss, R2 저장 
    avg_loss = total_loss / max(total, 1)
    r2_value = r2.compute().item()
    mse_value = mse.compute().item()

    return avg_loss, r2_value, mse_value


## ========================================================
## 함수이름 : show_predictions
## 반환결과 :  - 
## ========================================================
@torch.no_grad()
def show_predictions(model, loader, class_names, device, n=8):
    ##-> 예측 모드 설정
    model.eval()

    ##-> 배치 1개만 추출 : 샘플 몇 개만 테스트 진행 위해
    ##-> for x, y in loader: break와 동일
    x, y = next(iter(loader))
    x = x.to(device)

    logits = model(x)
    
    ##-> loss 계산/역전파가 끝난 뒤 지표용으로만 CPU로 내림
    pred = logits.argmax(dim=1).cpu()
    y = y.cpu()

    ##-> 배치에서 n개만 선택
    n = min(n, x.size(0))
    print("Sample predictions:")
    for i in range(n):
        gt   = class_names[y[i].item()]
        pd   = class_names[pred[i].item()]
        mark = "[O]" if gt == pd else "[X]"
        print(f"- GT: {gt:<5} | Pred: {pd:<5} {mark}")

## ========================================================
## 함수이름 : plot_history
## 반환결과 :  - 
## ========================================================
def plot_history(history, title="Training Curves"):
    epochs = list(range(1, len(history["train_loss"]) + 1))

    plt.figure(figsize=(12, 4))

    plt.subplot(1, 2, 1)
    plt.plot(epochs, history["train_loss"], label="train_loss")
    plt.plot(epochs, history["val_loss"],   label="val_loss")
    plt.xlabel("Epoch"); plt.ylabel("Loss")
    plt.title(f"{title} - Loss")
    plt.legend(); plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(epochs, [a * 100 for a in history["train_acc"]], label="train_acc (%)")
    plt.plot(epochs, [a * 100 for a in history["val_acc"]],   label="val_acc (%)")
    plt.xlabel("Epoch"); plt.ylabel("Accuracy (%)")
    plt.title(f"{title} - Accuracy")
    plt.legend(); plt.grid(True)

    plt.tight_layout()
    plt.show()