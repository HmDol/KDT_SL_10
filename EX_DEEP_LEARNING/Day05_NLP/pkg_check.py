## --------------------------------------------------------
## 개발환경 버전 체크 => 가상환경 이름 : NLP, PYTHON 버전 : 3.11
##                    GPU CUDA 버전: 12.4
## --------------------------------------------------------
import torch
import pandas as pd
import matplotlib as mp
import sklearn as sk
import numpy as np 

print(f"pytorch     v.{torch.__version__}")
print(f"pandas      v.{pd.__version__}")
print(f"matplotlib  v.{mp.__version__}")
print(f"sklearn     v.{sk.__version__}")
print(f"numpy       v.{np.__version__}")

if torch.cuda.is_available():
    print(f"torch.version.cuda : {torch.version.cuda}")
    print(f"current_device : {torch.cuda.current_device()}")
    print(f"device_name    : {torch.cuda.get_device_name()}")
    print(f"capability     : {torch.cuda.get_device_capability()}")
else:
    print("NO cuda")