# KOI 전자에서는 건강에 좋고 맛있는 훈제오리구이 요리를 간편하게 만드는 인공지능 오븐을 개발하려고 한다.
# 인공지능 오븐을 사용하는 방법은 적당한 양의 오리 훈제 재료를 인공지능 오븐에 넣으면 된다. 그러면 인공지능 오븐은 오븐구이가 끝나는 시간을 분 단위로 자동적으로 계산한다.
# 또한, KOI 전자의 인공지능 오븐 앞면에는 사용자에게 훈제오리구이 요리가 끝나는 시각을 알려 주는 디지털 시계가 있다.
# 훈제오리구이를 시작하는 시각과 오븐구이를 하는 데 필요한 시간이 분단위로 주어졌을 때, 오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하시오.

h, m = map(int, input().split())
cook_time = int(input()) # 분 단위로 입력
end_time = m + cook_time # cook_time이 분 단위로 입력되기 때문에 m + cook_time을 하면 end_time 이 된다.
m_2_h = end_time//60 # 60분마다 시간이 1개씩 늘어나므로 끝나는 분(minutes)/ 60(1시간)을 해줘야 한다

if h + m_2_h < 24 and end_time > 59:
    print(h + m_2_h, end_time - 60*m_2_h)
elif h + m_2_h > 23:
    print((h+m_2_h)-24, end_time - 60*m_2_h)
else:
    print(h, end_time)