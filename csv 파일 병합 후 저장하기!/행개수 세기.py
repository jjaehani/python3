import pandas as pd
import os

filePath = './fold/'  # 폴더 주소 입력

fileAll = os.listdir(filePath)

fileCsv = [filePath + file[:-4]
           for file in fileAll
           if file.endswith('.csv')]  # 파일 형태 .csv에만 적용

for file in fileCsv:
    df = pd.read_csv(file + '.csv')
    print(file, len(df))  # 파일명과 row 길이 출력
