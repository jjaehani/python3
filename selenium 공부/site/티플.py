# 라이브러리 선언
import time
from selenium import webdriver as wb  # webdriver를 실행 및 브라우저 제어를 위한 라이브러리
from selenium.webdriver.common.keys import Keys  # 키보드 값을 제어할 수 있는 라이브러리
from selenium.webdriver.common.by import By  # 요소를 접근하기 위한 방식을 활용할 수 있는 라이브러리

# 링크(domain)이동
url = "https://www.tple.co.kr/"  # URL 정의

driver = wb.Chrome()  # 브라우저 실행
driver.get(url)

# 로그인 버튼 클릭
driver.find_element(By.XPATH, '//*[@id="account"]/div/button').click()

# id, pw 입력
driver.find_element(By.XPATH, '//*[@id="userId"]').send_keys('dkdiwaz1234')  # id 입력

user_pw = driver.find_element(By.XPATH, '//*[@id="userPw"]')
user_pw.send_keys('idkwm12345')  # pw 입력
user_pw.send_keys(Keys.ENTER)  # 엔터키 입력

# 카테고리 선정
category = driver.find_element(By.XPATH, '//*[@id="code119"]')
category.click()

limit = driver.find_element(By.XPATH, '//*[@id="listScale100"]/button')
limit.click()

# 카테고리 게시물 전체 갯수 계산
count = 0
while True:
    count += 1
    try:
        driver.find_element(By.XPATH, '//*[@id="divFileList"]/div[2]/span/a[13]').click()
        time.sleep(1)
    except:

        break

total = 25 * count

# 결과 저장
result = ('싸다파일 - 영화 -', total)
print(result, file=open('../x결과.txt', 'w', encoding='utf-8'))
