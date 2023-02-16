repeat = int(input())
genius = []

for i in range(repeat):
    try:
        num = list(map(int,input().split()))
        avg = sum(num[1:]) / num[0]
        num.pop(0)

        for j in range(len(num)):
            if num[j] > avg:
                genius.append(num[j])
        print(("{:.3f}".format(100 / (len(num) / len(genius)))),'%',sep='')
        genius.clear()
    except ZeroDivisionError:
        print("{:.3f}".format(0),'%',sep='')
        genius.clear()