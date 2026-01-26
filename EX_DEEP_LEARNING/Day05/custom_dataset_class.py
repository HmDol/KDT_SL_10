## ========================================================
## Filename     : custom_class.py
## Description  : 사용자 데이터 전용 Dataset, Model 및 클래스들
## =======================================================
## 모듈 로딩
import torch
import torch.nn as nn
import torch.nn.functional as F
from   torch.utils.data import Dataset
import numpy as np

    
## ========================================================
## 클래스이름 : EagerDataset
## 부모클래스 : Dataset
## 방     식 : 일괄 처리 방식의 Dataset
## 특     징 : 초기화 시에 모든 데이터를 Tensor화 진행
##            빠르지만, 대량 데이터의 경우 OOM(Out Of Memory) 발생
## ========================================================
class EagerDataset(Dataset):

    def __init__(self, featureDF, targetDF):
        super().__init__()
        self.xTS = torch.tensor(featureDF.values, dtype=torch.float32)
        self.yTS = torch.tensor(targetDF.values, dtype=torch.float32) 
        self.length = featureDF.shape[0]

    def __len__(self):
        return self.length
    
    def __getitem__(self, idx):
        return self.TS[idx], self.yTS[idx]
    
## ========================================================
## 클래스이름 : OnTheFlyDataset
## 부모클래스 : Dataset
## 방     식 : 즉시 처리 방식의 Dataset
## 특     징 : 데이터양이 작을 때 / 텐서 변환이 자주 발생 => 속도 느려질 수 있음
## ========================================================
class OnTheFlyDataset(Dataset):
    def __init__(self, featureDF, targetDF):
        super().__init__()
        self.x = featureDF.values
        self.y = targetDF.values 

    def __len__(self):
        return self.x.shape[0]
    
    def __getitem__(self, idx):
        xTS = torch.tensor(self.x[idx], dtype=torch.float32)
        yTS = torch.tensor(self.y[idx], dtype=torch.float32)
        return xTS, yTS
    

## ========================================================
## 클래스이름 : NomalDataset
## 부모클래스 : Dataset
## 방     식 : 공유 방식 Dataset
## 특     징 : 일반적으로 많이 사용 되고, 많은 데이터양에도 안정적
##            메모리 사용량, 속도는 다른 2가지 방식에 비해서 보통
## ========================================================
class NomalDataset(Dataset):
    ## ★★★ copy=False : dtype이 같을 경우 복사본 생성X
    def __init__(self, featureDF, targetDF):
        self.x = featureDF.values.astype("float32", copy=False)
        self.y = targetDF.values.astype("float32", copy=False)

    def __len__(self):
        return self.x.shape[0]

    def __getitem__(self, i):
        ##- torch.from_numpy() 복사 없이 공유(view)
        xTS = torch.from_numpy(self.x[i])   
        yTS = torch.from_numpy(self.y[i])
        return xTS, yTS

## ========================================================
## 클래스이름 : MemmapDataset
## 부모클래스 : Dataset
## 데이터크기 : 수GB~수십GB급 데이터
## 처리방식(1) 메모리맵(memmap)
## - 파일을 메모리에 다 올리지 않고 필요한 부분만 OS가 페이지 단위로 읽어줌
## - __getitem__()으로 랜덤 접근 가능 
## 조건
## - 데이터 파일을 .npy 또는 raw binary로 저장
## ========================================================
class MemmapDataset(Dataset):
    
    def __init__(self, x_path, y_path, n_rows, n_features,
                 x_dtype="float32", y_dtype="float32"):
        super().__init__()

        self.n_rows     = int(n_rows)
        self.n_features = int(n_features)

        ## memmap: 파일을 배열처럼 접근
        ##         실제 로딩은 OS가 필요할 때 수행
        self.x_mm = np.memmap(x_path, mode="r", 
                              dtype=np.dtype(x_dtype),
                              shape=(self.n_rows, self.n_features) )

        self.y_mm = np.memmap(y_path,
                              mode="r",
                              dtype=np.dtype(y_dtype),
                              shape=(self.n_rows,) )

    def __len__(self):
        return self.n_rows

    def __getitem__(self, idx):
        # numpy view -> torch tensor (복사 최소화)
        x = torch.from_numpy(np.array(self.x_mm[idx], copy=False)).float()

        y_np = np.array(self.y_mm[idx], copy=False)
        y = torch.tensor(y_np).float()  # 회귀/이진분류면 float 권장

        return x, y
    
## ========================================================
## 클래스이름 : StreamingCSVDataset
## 부모클래스 : Dataset
## 데이터크기 : 수GB~수십GB급 데이터
## 처리방식(2) 스트리밍용 - 파일 순차 읽기
## - 초대용량 CSV 스트리밍 (IterableDataset)
## - CSV/TSV 같은 텍스트 파일을 줄 단위로 흘려보내는 방식
## - 랜덤 접근 어려워 shuffle=False, 필요하면 샤딩(shard)
## - num_workers 사용 시 worker별로 데이터를 나눠 읽도록 처리
## 샤딩(shard)
## - 하나의 거대한 데이터를 여러 개의 조각(shard)으로 나누어
##   각 프로세스(또는 worker)가 서로 다른 조각을 처리하도록 하는 방식
## ========================================================
import csv
import torch
from torch.utils.data import IterableDataset, get_worker_info

class StreamingCSVDataset(IterableDataset):
    
    def __init__(self, csv_path, has_header=True):
        super().__init__()
        self.csv_path = csv_path
        self.has_header = has_header

    def _line_iterator(self):
        with open(self.csv_path, "r", encoding="utf-8", newline="") as f:
            reader = csv.reader(f)
            if self.has_header:
                next(reader, None)
            for row in reader:
                yield row

    def __iter__(self):
        it = self._line_iterator()

        # DataLoader worker 병렬일 때, worker별로 라인을 분배
        info = get_worker_info()
        if info is not None:
            worker_id = info.id
            num_workers = info.num_workers

            # 간단한 방식: worker_id에 해당하는 라인만 받기 (round-robin)
            for i, row in enumerate(it):
                if (i % num_workers) == worker_id:
                    yield self._parse_row(row)
        else:
            for row in it:
                yield self._parse_row(row)

    def _parse_row(self, row):
        # 예시: 마지막 컬럼이 label, 나머지가 feature라고 가정
        *feat, label = row
        x = torch.tensor([float(v) for v in feat], dtype=torch.float32)
        y = torch.tensor(float(label), dtype=torch.float32)
        return x, y

import random 

## ========================================================
## 다양한 종류의 Random 난수 재현성 설정 방법들
## ========================================================
def seed_everything(seed=42):
    # -------------------------------
    # Python 표준 라이브러리 random 모듈의 난수 시드 고정
    #  - random.random(), randint(), shuffle() 등 
    #    random 모듈 기반 난수 결과를 재현 가능하게 함
    random.seed(seed)

    # NumPy의 난수 시드 고정
    #  - np.random.rand(), np.random.randn(), np.random.shuffle() 등 
    #    NumPy RNG 결과를 재현 가능하게 함
    np.random.seed(seed)

    # PyTorch의 CPU RNG 시드 고정
    #  - CPU에서 생성되는 난수(예: torch.rand, torch.randn, 
    #    Dropout/초기화 등 CPU 경로)를 재현 가능하게 함
    torch.manual_seed(seed)

    # PyTorch의 CUDA(GPU) RNG 시드 고정 (모든 GPU 장치에 적용)
    #  - GPU에서 생성되는 난수(예: torch.rand(..., device='cuda'), CUDA Dropout/초기화 등)를 재현 가능하게 함
    #  - 멀티 GPU 사용 시 각 GPU의 RNG도 함께 고정
    torch.cuda.manual_seed_all(seed)