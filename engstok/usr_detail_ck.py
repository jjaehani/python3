import pymysql

connect = pymysql.connect(host='localhost', user='root', password='1234',
                          db='entok_rootdb', charset='utf8mb4')

user_input = input("값을 입력하세요: ")

cur = connect.cursor()

query = "SELECT company_name_kor, user_name, user_title FROM INFO_USER_TB WHERE user_key = %s"
cur.execute(query, (user_input,))

connect.commit()

datas = cur.fetchall()
cnt = 0
l = ['회사명: ', '회원이름: ', '직책: ']

if datas:
    for data in datas:
        for i, column in enumerate(data):
            print(f"{l[i]} {column}")
        print("-------------------------")
else:
    print("조회되는 값이 없습니다.")

cur.close()