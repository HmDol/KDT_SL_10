# ## --------------------------------------------------------------
# ## 내부 패키지 활용하기
# ## --------------------------------------------------------------

# ## [1] 기본 형태
# import calcpkg.geometry as geo
# import calcpkg.operation as op

# print(geo.rectangle_area(10,4))
# print(geo.triangle_area(8,10))


# ## [2] __init__.py를 활용한 간략화 형태
# import calcpkg as c

# print(c.geometry.rectangle_area(10,4))
# print(c.geometry.triangle_area(8,10))


#  ## [2-2] 하위 모듈 바로 사용 가능
# from calcpkg import *
# print(geometry.triangle_area(8,10))

## [3] 패키지 내 모듈들의 모든 것을 import
from calcpkg import *

print(triangle_area(8,10))
print(add(8,10))
