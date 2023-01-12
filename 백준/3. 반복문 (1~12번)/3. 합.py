# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

n = int(input())
n1 = 0
total = []

while n1 < n:
    n1 = n1 + 1
    total.append(n1)

print(sum(total))


