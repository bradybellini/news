from supapsql import SupaPSQL
from rssparser import RSSParser


r = RSSParser()
articles = r.articles("https://www.gameinformer.com/rss.xml", "b52da7d9-1a18-4ce3-af41-546f6568f127")

# articles = r.articles("https://www.newyorker.com/feed/everything", "d30d7c83-0ebc-44b7-8935-012d4125e5c7")

# print(articles)
# supa = SupaPSQL()

# insert = supai.insert("https://www.gameinformer.com/rss.xml", "b52da7d9-1a18-4ce3-af41-546f6568f127")
# supa.run()

# print(insert)

