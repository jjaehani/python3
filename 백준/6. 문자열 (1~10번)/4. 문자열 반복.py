# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
# 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.
# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

a = int(input())
new_list = []

for i in range(a):
    new_list.clear()
    r, s = (input().split())  # r = 반복 횟수 s = 문자
    n = list(s)
    cnt = 0

    for j in range(int(r)+1): # r만큼 반복

        if cnt >= len(n):
            break

        elif int(r) < len(n):
            for k in range(len(n)):  # r만큼 반복
                repeat = n[cnt] * int(r)  # 첫번째는 cnt가 0이므로 리스트 n[0] * int(r) 두번째는 cnt 가 1이므로 n[1] * int(r) ...
                cnt += 1
                new_list.append(repeat)
                str1 = ''.join(str(s) for s in new_list)  # 리스트 출력(괄호, 공백, '' 제거)

                if cnt >= len(n):
                    break

        else:
            repeat = n[cnt] * int(r)  # 첫번째는 cnt가 0이므로 리스트 n[0] * int(r) 두번째는 cnt 가 1이므로 n[1] * int(r) ...
            cnt += 1
            new_list.append(repeat)
            str1 = ''.join(str(s) for s in new_list)  # 리스트 출력(괄호, 공백, '' 제거)

    print(str1)

