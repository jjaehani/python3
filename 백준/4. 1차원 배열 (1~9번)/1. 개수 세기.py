# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.

n = int(input())
mylist = list(map(int,input().split()))

# v의 값이 목록에 몇 개 포함되어 있는지를 확인
v = int(input())
cnt = mylist.count(v)
print(cnt)