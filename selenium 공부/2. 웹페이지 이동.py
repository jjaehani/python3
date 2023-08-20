from selenium import webdriver # 라이브러리 선언

driver = webdriver.Chrome('./chromedriver') # 드라이버 위치 설정

baseUrl ="https://www.naver.com" # URL 정의
driver.get(baseUrl) # URL 이동
driver.current_url # 현재 URL 정보

