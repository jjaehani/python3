import requests
import json

city = input() #도시
apiKey = "e739b833f21254f7d41b85cf9a0978d4"
lang = 'kr' #언어
units = 'metric' #화씨 온도를 섭씨 온도로 변경
api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang={lang}&units={units}"

result = requests.get(api) # api 값 받아오기
result = json.loads(result.text)

name = result['name']
lat = result['coord']['lat']
weather = result['weather'][0]['description']
temp = result['main']['temp']
humidity = result['main']['humidity']
wind = result['wind']['speed']
wind_chill = result['main']['feels_like']
# wind_chill = 13.12 + (0.6215 * temp) -11.37 * wind ** 0.16 + 0.3965 * wind ** 0.16 * temp

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

print('지역:',name)
print('날씨:',weather)
print('온도: ', round(temp, 1),'°c',sep='' )
print('습도:', humidity)
print('체감온도: ', round(wind_chill, 1),'°c',sep='' )
