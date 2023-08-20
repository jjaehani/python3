# image_crawling/image_crawling.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

keyword = input("수집하고 싶은 연예인? : ")

#웹
## 네이버 이미지 접속
print('[ 접속중... ]')
driver = webdriver.Chrome('../chromedriver')
driver.implicitly_wait(15)
driver.maximize_window() #최대화

url = 'https://search.naver.com/search.naver?where=image&query={}'.format(keyword)
driver.get(url)

## 페이지 아래로 내리기
body = driver.find_element(By.CSS_SELECTOR,'body')

##스크롤 다운 - 5회
for i in range(10):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1) # 활성화 기다려주기

# 이미지 요소 모두 찾기
imgs = driver.find_elements(By.CSS_SELECTOR, 'img._img')
# print(len(imgs))

## 이미지 링크 추출
links = []
for img in imgs:
    link = img.get_attribute('src')
    if 'http' in link: # 반드시 이미지 주소에 http가 들어간 것만 추출
        links.append(link)

driver.close()
print('[ 정보 수집 완료 ] ')

## 폴더 생성
import os
if not os.path.isdir('./{}'.format(keyword)): #만들려고 하는 디렉토리 있는지 확인
    os.mkdir('./{}'.format(keyword)) #없으면 생성
print('[ 폴더 생성 중 ] ')

## 다운로드
print('[ 다운로드 중 ] ')
from urllib.request import urlretrieve
from tqdm import tqdm

for index, link in tqdm(enumerate(links),total=len(links)):
    # 확장자가 무엇인지 추출
    start = link.rfind('.')
    end = link.rfind('&')

    file_type = link[start:end] # 확장자 : .jpg
    filename = './{0}/{0}{1:03d}{2}'.format(keyword, index, file_type)  # 파일명 : 아이스크림001.jpg
    urlretrieve(link, filename)

print('[ 다운로드 완료 ] ')


#압축 - 메일
import zipfile
zip_file = zipfile.ZipFile('./{}.zip'.format(keyword),'w')

# print(os.listdir('./{}'.format(keyword)))
for image in os.listdir('./{}'.format(keyword)):
    print(image,"압축파일에 추가중")
    zip_file.write('./{}/{}'.format(keyword,image), compress_type=zipfile.ZIP_DEFLATED)
zip_file.close()
print("압축완료")