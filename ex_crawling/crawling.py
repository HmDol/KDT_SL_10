import re
from selenium import webdriver                           ## 웹페이지 드라이버 사용하기 위한 라이브러리
from selenium.webdriver.chrome.service import Service    ## 크롬 브라우저 서비스 모듈
from selenium.webdriver.chrome.options import Options    ## 크롬 브라우저 옵션 설정 모듈
from bs4 import BeautifulSoup                           ## html 코드 가져오기 위한 라이브러리
import pandas as pd
import time



CHROME_DRIVER_PATH = "./chromedriver-win64/chromedriver.exe"

options = Options()
options.add_argument("--headless")    # 창 표시 옵션
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

years = [2020, 2021, 2022, 2023, 2024, 2025]

## 가져온 데이터를 수집하기 위한 딕셔너리
data_list = []

for y in years:  # 수집할 연도
    for m in range(1,13): # 수집할 월
        if y ==2025 and m>9:
            break
        url = f"https://auto.danawa.com/newcar/?Work=record&Tab=Top10&Brand=303,307,304,312,326,611&Month={y}-{m:02d}-00"
        
        ## 크롬드라이버에 url 넘기기
        driver.get(url)

        # 페이지 대기
        time.sleep(2)

        print(f'[{y}-{m:02d}] 페이지 데이터 수집')
        html_code_to_str =  BeautifulSoup(driver.page_source, "html.parser")
        div = html_code_to_str.find("div", class_="recordSum clearFix")
        if not div:
            print(f'{y}-{m:02d} 페이지 구조에 데이터 없음')
            continue
        ul = div.find("ul", class_ = "sumfuel")
        current_month_data = {'Year': y, 'Month': m}
        if ul:
            for li in ul.find_all("li", recursive=False):
                ## 오류 예외처리를 위한 try, except 문
                try:
                ## 연료 이름 변수에 저장
                    fuel_name = li.text.split(' ')[0]
                    ## 연료이름 가솔린이거나 전기면 저장로직 진행
                    if fuel_name == '가솔린' or fuel_name == '전기':    
                        count_tag = li.find('strong')
                        if count_tag:
                            count_text = count_tag.text.replace(",", "") # 판매 대 수 천단위 쉼표제거
                            count_text_changeType_int = int(count_text)
                            current_month_data[fuel_name] = count_text_changeType_int
                except Exception as e:
                    print(f'{y}-{m:02d} 페이지 데이터 추출 실패 오류 발생 {e}')
                    print("다음페이지 수집 진행")
                    continue
        data_list.append(current_month_data)

# driver.quit()

df = pd.DataFrame(data_list)

df.to_csv('./전기차_가솔린차_판매량_2020_2025.csv',encoding='utf-8-sig', index=False)
print("데이터 수집 끝")



