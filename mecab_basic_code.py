import subprocess
import pandas as pd

def run_mecab(text):
    command = ['/usr/local/bin/mecab']
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate(input=text.encode('utf-8'))
    return stdout.decode('utf-8')

# CSV 파일에서 df 읽기
df = pd.read_csv('../data.csv', usecols=[12])
results = []

# 데이터프레임의 각 행을 반복하여 mecab 실행
for index, row in df.iterrows():
    text = str(row[0])
    result = run_mecab(text)
    results.append(result)
result_df = pd.DataFrame({'Mecab_Result': results})
result_df.to_excel('mecab_results.xlsx', index=False)
