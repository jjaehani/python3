repeat = int(input())
score = 0
continuity = 1
for i in range(repeat):
    ans = list(input())

    for j in range(len(ans)):

        if ans[j-1] =='O' and ans[j] == 'O' and j > 0:
            score += continuity + 1
            continuity += 1

        elif ans[j] == 'O'and ans[j-1] != 'O'and j > 0:
            score += 1
            continuity = 1

        elif ans[j] == 'X':
            continuity = 1

        else:
            score +=1

    print(score)
    score = 0
    continuity = 1

