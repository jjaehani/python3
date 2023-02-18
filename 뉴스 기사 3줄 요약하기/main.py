import feedparser
from newspaper import Article
from summa.summarizer import summarize

#res 링크 저장
rss_url = "http://feeds.feedburner.com/inven"

#rss 피드에 저장된 데이터를 rss_feed에 저장한다.
rss_feed = feedparser.parse(rss_url)

#rss fee에는 총 25개의 뉴스 기사만 보여짐을 확인 할 수 있다.
print(len(rss_feed.entries))

#p속에 rss_feed의 리스트 크기 (25)만큼 반복한다.
for p in rss_feed.entries:

    #rss_feed 속 뉴스 링크 분류
    url = p.link

    article= Article(url, language = 'ko')
    article.download()
    article.parse()

    NewsFeed = article.text
    NewsSum = summarize(NewsFeed)

    print(article.title + '\n')

    print(NewsFeed + '\n')

    print(NewsSum + '\n')
