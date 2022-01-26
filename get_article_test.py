import feedparser

d = feedparser.parse('https://kotaku.com/rss')


# print(d.entries[1]['title'])
for i in range(len(d.entries)):
    print(d.entries[i].title)