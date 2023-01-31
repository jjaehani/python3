import requests
import json
import re

# line 6 ~ 22 : api로 날씨 데이터 받아오기
city = input() # 도시명 입력받기
apiKey = "e739b833f21254f7d41b85cf9a0978d4" # 개인 고유 api키값
lang = 'kr' # 언어
units = 'metric' # 화씨 온도를 섭씨 온도로 변경
api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang={lang}&units={units}" # api 링크

result = requests.get(api) # api 값 받아오기
result = json.loads(result.text)

name = result['name']                               # 지역명
weather = result['weather'][0]['description']       # 날씨
temp = result['main']['temp']                       # 온도
humidity = result['main']['humidity']               # 습도
wind = result['wind']['speed']                      # 풍속
wind_chill = result['main']['feels_like']           # 체감온도
# wind_chill = 13.12 + (0.6215 * temp) -11.37 * wind ** 0.16 + 0.3965 * wind ** 0.16 * temp
############################################################################################################################

# line 26 ~ 71 : 영어 -> 한글로 번역
def get_translate(text):
    client_id = "0xQ7we9y2nbJPMGmptLb"      # 개인 client_id 값
    client_secret = "HdwJkw4rSn"            # 개인 client_secret 값

    data = {'text' : text,
            'source' : 'en',
            'target': 'ko'}

    url = "https://openapi.naver.com/v1/papago/n2mt"

    header = {"X-Naver-Client-Id":client_id,
              "X-Naver-Client-Secret":client_secret}

    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code

    if(rescode==200):
        send_data = response.json()
        trans_data = (send_data['message']['result']['translatedText'])
        return trans_data
    else:
        print("Error Code:" , rescode)

def start_trans(input_text):
    ENGS = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k',
            'K', 'l', 'L',
            'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w',
            'W', 's', 'S', 'y', 'Y', 'z', 'Z']

    KORS = ['에이', '에이', '비', '비', '씨', '씨', '디', '디', '이', '이', '에프', '에프', '쥐', '쥐', '에이치', '에이치', '아이', '아이', '제이',
            '제이',
            '케이', '케이', '엘', '엘', '엠', '엠', '엔', '엔', '오', '오', '피', '피', '큐', '큐', '알', '알', '에스', '에스', '티', '티', '유',
            '유', '브이', '브이',
            '더블유', '더블유', '에스', '에스', '와이', '와이', '지', '지']

    trans = dict(zip(ENGS, KORS))
    papago_trans = get_translate(input_text) # 파파고로 번역 데이터 보내기
    is_english = re.compile('[-a-zA-Z]')
    temp = is_english.findall(papago_trans) # 파파고에서 번역이 안된 영어 문장이 있다면 temp값 존재

    result_trans = []
    if len(temp) > 0: # 영어 데이터 존재 유무
        result_trans = ''.join([trans[i] for i in temp])
        return result_trans # 한글로 번역이 안된 데이터 존재
    else:
        return papago_trans # 한글로 번역이 잘된 데이터일 경우 그대로 리턴



############################################################################################################################
print('***** 오늘의 추천 착장입니다. *****')

# 기온별 착장 추천
if wind_chill < 5:
    print('패딩, 두꺼운코트, 누빔옷, 기모, 목도리')
elif wind_chill >=5 and wind_chill < 9:
    print('울코트, 히트텍, 가죽옷, 기모')
elif wind_chill >=9 and wind_chill < 12:
    print('트렌치코트, 야상, 점퍼, 기모바지')
elif wind_chill >=12 and wind_chill < 17:
    print('자켓, 가디건, 청자켓, 니트, 청바지, 스타킹')
elif wind_chill >=17 and wind_chill < 20:
    print('얇은가디건, 블라우스, 맨투맨, 후드, 긴바지')
elif wind_chill >=20 and wind_chill < 23:
    print('얇은 셔츠, 반팔, 반바지, 면바지')
elif wind_chill >=23 and wind_chill < 28:
    print('얇은 셔츠, 반팔, 반바지, 면바지')
elif wind_chill >=28:
    print('민소매, 반팔, 반바지, 린넨의류')

print('*****************************', '\n')

a = start_trans(name) # 영어 -> 한글로

print('지역:',a)
print('날씨:',weather)
print('온도: ', round(temp, 1),'°c',sep='' )
print('습도:', humidity)
print('체감온도: ', round(wind_chill, 1),'°c',sep='' )
