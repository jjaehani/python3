# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.


srt = input()
y = list(srt.upper())

n = []
cnt = 0

for i in range(len(y)):
        k = y.count(y[cnt])
        cnt+=1
        n.append(int(k))

if int(max(n)) < int(n.count(max(n))):
    print('?')

else:
    print(max(y, key=y.count))