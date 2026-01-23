import torch
import matplotlib.pyplot as plt

## ========================================================
## 함수이름 : train_one_epoch
## 반환결과 : 손실, 정확도
## ========================================================
def train_one_epoch(model, loader, loss_fn, optim, device):
    ## 모델 동작모드 설정 : 반드시 학습 전에 설정
    model.train()
    
    ## 1에포크 후 학습 결과 저장용
    total_loss, correct, total = 0.0, 0, 0

    ## 배치크기만큼 학습 진행
    for x, y in loader:
        x, y = x.to(device), y.to(device)

        ## 순전파
        logits = model(x)
        loss = loss_fn(logits, y)

        ## 역전파
        optim.zero_grad()
        loss.backward()
        optim.step()

        ## 학습 결과 계산 및 저장
        total_loss += loss.item() * x.size(0)
        pred = logits.argmax(dim=1)
        correct += (pred == y).sum().item()
        total += x.size(0)

    return total_loss / total, correct / total


## ========================================================
## 함수이름 : evaluate
## 함수기능 : 검증/테스트 시 사용
##           역전파 진행 하지 않음!!!!
## 반환결과 : 손실, 정확도
## ========================================================
@torch.no_grad()
def evaluate(model, loader, loss_fn, device):
    ## 모델 동작 모드 => 학습에 필수적인 긴으들 비활성화
    model.eval()
    ## 검증시 결과 저장변수들
    total_loss, correct, total = 0.0, 0, 0
    
    ## 검증/테스트용 배치크기만큼 로딩 후 예측 진행
    for x, y in loader:
        ## 피쳐, 타겟 추출 후 위치 설정
        x, y = x, y = x.to(device), y.to(device)

        ## 순전파
        logits = model(x)
        loss = loss_fn(logits, y)

        ## 예측 결과 저징
        total_loss += loss.item() * x.size(0)
        pred = logits.argmax(dim=1)
        correct += (pred == y).sum().item()
        total += x.size(0)

    return total_loss / total, correct / total


## ========================================================
## 함수이름 : show_predictions
## 반환결과 :  - 
## ========================================================
@torch.no_grad()
def show_predictions(model, loader, class_names, device, n=8):
    model.eval()

    x, y = next(iter(loader))
    x = x.to(device)

    logits = model(x)
    pred = logits.argmax(dim=1).cpu()
    y = y.cpu()

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