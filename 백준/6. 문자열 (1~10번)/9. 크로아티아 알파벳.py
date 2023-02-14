n = list(input())
cnt_list=[]
cnt = 0

# 크로아티아 알파벳으로 합치기
for j in range(len(n)):
    if n[cnt] == '=' and n[cnt-1] == 'z' and n[cnt-2] == 'd':        # dz=
        n[cnt] = (n[cnt - 2] + n[cnt - 1] + n[cnt])
        cnt_list.append(cnt - 1)
        cnt_list.append(cnt - 2)

    elif n[cnt] == '=' or n[cnt] == '-':                            # c= s= z= / c- d-
        n[cnt] = (n[cnt-1]+n[cnt])
        cnt_list.append(cnt-1)

    elif n[cnt] == 'j' and (n[cnt-1] =='l' or n[cnt-1] =='n'):      # nj lj
        n[cnt] = (n[cnt - 1] + n[cnt])
        cnt_list.append(cnt - 1)

    cnt+=1

# cnt_list 내림차순 정렬
cnt_list.sort(reverse=True)

for i in range(len(cnt_list)):
    n.pop(cnt_list[i])

print(len(n))