import pymysql

connect = pymysql.connect(host='localhost', user='root', password='1234',
                          db='entok_rootdb', charset='utf8mb4')

user_inputs = list(map(input, ["성함을 입력하세요: ", "메일을 입력하세요: "]))
cur = connect.cursor()
# INFO_USER_TB
query = "SELECT user_key FROM INFO_USER_TB WHERE user_name = %s AND user_email = %s"
cur.execute(query, user_inputs)

connect.commit()

datas = cur.fetchone()
user_input = datas[0]
cur = connect.cursor()

query = "SELECT insert_date, end_date, category, " \
        "model_name, manufacturer, amount, sell_total_fee FROM INFO_PUR_REQ_TB WHERE user_key = %s"

cur.execute(query, (user_input,))
connect.commit()
datas = cur.fetchall()

l = ['접수일자: ', '완료일자: ', '카테고리: ', '모델명: ', '제조사: ', '주문수량: ', '총 구매가격: ']

if datas:
    for data in datas:
        for i, column in enumerate(data):
            print(f"{l[i]} {column}")
        print("-------------------------")
else:
    print("조회되는 값이 없습니다.")

cur.close()