# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
a, b = map(int, input("정수 두개를 입력하십시오 : ").split())
print(a+b)

# 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.
a, b = map(int, input().split())
print(a-b)

# 두 정수 A와 B를 입력받은 다음, A×B를 출력하는 프로그램을 작성하시오.
a, b = map(int, input().split())
print(a*b)

# 두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.
a, b = map(int, input().split())
print(a/b)

# 두 자연수 A와 B가 주어진다.
# 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.
a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a%b)