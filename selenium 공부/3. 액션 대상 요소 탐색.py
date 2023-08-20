from selenium import webdriver # 라이브러리 선언
# 드라이버 위치 설정
driver = webdriver.Chrome('./chromedriver')

# URL 정의
baseUrl ="https://www.naver.com"
# URL 이동
driver.get(baseUrl)
# 현재 URL 정보
driver.current_url


# 웹 페이지에서 원하는 요소 선택 (우클릭 후 검사) 이후 소스코드 영역에서 우클릭 후 COPY X PATH (* 클래스 속성으로 등으로도 접근가능)
serchPath = '//*[@id="menu-item-382"]'