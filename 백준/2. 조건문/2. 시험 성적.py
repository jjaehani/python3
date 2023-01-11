# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
while True:
    score = int(input())

    if score > 100 or score < 0:
        print('점수를 제대로 확인 후 다시 입력하십시오.')

    elif score >= 90 and score <= 100:
        print('A')
        break

    elif score >= 80 and score <= 89:
        print('B')
        break

    elif score >= 70 and score <= 79:
        print('C')
        break

    elif score >= 60 and score <= 69:
        print('D')
        break

    else:
        print('F')
        break

