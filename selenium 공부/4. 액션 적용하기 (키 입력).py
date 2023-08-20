from selenium.webdriver.common.keys import Keys
from selenium import webdriver # 라이브러리 선언
# 드라이버 위치 설정
driver = webdriver.Chrome('./chromedriver')

# URL 정의
googleUrl = 'https://www.google.co.kr'
# URL 이동
driver.get(googleUrl)
# 요소 탐색
searchPath = '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input'
driver.find_element_by_xpath(searchPath).send_keys("selenium wiki")
driver.find_element_by_xpath(searchPath).send_keys(Keys.ENTER)