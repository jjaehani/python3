# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

ran = int(input())
num = int(input())
n = list(map(int, str(num)))
k = sum(n[0:])
print(k)