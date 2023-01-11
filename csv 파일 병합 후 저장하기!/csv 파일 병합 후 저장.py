import pandas as pd

# 파일을 2개 이상 병합하길 원한다면 file_3 = './파일명.csv' 형식으로 쭉쭉 원하는 병함개수만큼 늘리시면 됩니다.
file_1 = './파일명.csv'
file_2 = './파일명.csv'
# file_3 = './파일명.csv'
# file_4 = './파일명.csv'
#           :
#           :
# file_n = './파일명.csv'

print("*** 여러 csv 파일을 하나의 pandas dataframe으로 병합 중입니다. ***")

# file_n 까지 늘어난 만큼 (map(pd.read_csv, [file_1, file_2, ... ,  file_n]) 으로 바꾸신 후 실행하면 됩니다.
dataFrame = pd.concat(map(pd.read_csv, [file_1, file_2]), ignore_index=True)
print(dataFrame)

df = pd.DataFrame(dataFrame)
df.to_csv("./원하는 파일명.csv", index = False)