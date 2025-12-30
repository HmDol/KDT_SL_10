## 폴더 패키지화를 위한 파일, 내용 없어도 됨

## [2] 다른 파일에 import 간략화
# from . import operation
# from . import geometry

## [3] 다른 파일에 import 간략화
## 패키지내 모듈들의 모든 것을 import
# from .operation import *
# from .geometry import * 


## [4] 패키지 내 모듈들의 일부만 공개하도록 설정
## __all__ => 매직변수코드에 설정
__all__ = ['add', 'mul', 'triangle_area']
from .operation import *
from .geometry import * 

print('__init__.py')
