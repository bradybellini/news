from supapsql import SupaPSQL
from rssparser import RSSParser


r = RSSParser()
articles = r.articles("https://kotaku.com/rss", "f70bd78d-71b0-4fae-9d15-9b321eb0fd75")


# print(articles[5])
# articles = r.articles("https://www.huffpost.com/section/front-page/feed", "42d45f8b-491b-432c-88bf-a78d9ae1b87b")

# articles = r.articles("https://www.newyorker.com/feed/everything", "d30d7c83-0ebc-44b7-8935-012d4125e5c7")

# print(articles)
# print(articles.remove())

for i in range(len(articles)):
#     print(articles[i])
    # print(i)
    if "elden" in articles[i]['title'].casefold():
        articles.pop(i)
    print(articles[i]['title'])

# supa = SupaPSQL()
# supa.run()


