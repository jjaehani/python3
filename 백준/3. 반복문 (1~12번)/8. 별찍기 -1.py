# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

x = int(input())
y = 0
for i in range(x):
    y = y+1
    print('*'* y)