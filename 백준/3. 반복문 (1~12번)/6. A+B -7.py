# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

x = int(input())
i = 0
while i < x:
    a, b = map(int,input().split())
    i = i+1
    print('Case','#%d:'%i, a+b)