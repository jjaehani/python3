# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

num = int(input())
n = list(map(int,input().split()))
n.sort()
print(n[0], n[-1])
