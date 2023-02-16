# 입력받기
repeat = int(input())
cnt_list=[]

cnt = 0
group_word = 0

# 문자 분리
for i in range(repeat):
    letter = list(input())

    for j in range(len(letter)):
        if cnt == 0:
            cnt+=1
            continue

        elif letter[cnt-1] == letter[cnt] and cnt > 0:
            cnt_list.append(cnt - 1)

        cnt+=1
    cnt = 0

    # cnt_list 내림차순 정렬
    cnt_list.sort(reverse=True)

    for k in range(len(cnt_list)):
        letter.pop(cnt_list[k])
    cnt_list.clear()
    result = set(letter)

    if len(result) == len(letter):
        group_word += 1
    else:
        continue

print(group_word)