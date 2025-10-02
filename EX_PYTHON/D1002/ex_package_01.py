## ------------------------------------------------------------------==
## 패키지 사용하기
## - 패키지 : 유사한 기능/목적의 모듈들을 하나로 묶어서 관리하는 것
## - 사  용 : import 패키지명.모듈명 (as 약칭)
##            from 패키지명.모듈명 import 변수||함수||클래스
## ------------------------------------------------------------------==
## 모듈 로딩
## ------------------------------------------------------------------==
import urllib.request as req    # 모듈명 그대로 사용

## ------------------------------------------------------------------==
## 묘듈의 변수, 함수, 클래스 사용 => 모듈명.변수명 / 모듈명.함수명()
## ------------------------------------------------------------------==
data = req.urlopen("https://naver.com")
print(f'data = > {type(data)}')
print(f'data.url = > {data.url}')
print(f'data.status = > {data.status}')
print(f'data = > {data.read()}')

#req.urlretrieve(url, filename) : 해당 url을 파일로 저장
img_url = "data:image/png;base64,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"
req.urlretrieve(img_url,"google.jpg")