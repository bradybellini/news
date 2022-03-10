from supapsql import SupaPSQL
from rssparser import RSSParser
from filter import ArticleFilter
import spacy
from spacy import displacy

ner = spacy.load("en_core_web_trf")
raw_text="The Indian Space Research Organisation or is the national space agency of India, headquartered in Bengaluru. It operates under Department of Space which is directly overseen by the Prime Minister of India while Chairman of ISRO acts as executive of DOS as well."
text1= ner(raw_text)
for word in text1.ents:
    print(word.text,word.label_)


# list1 = ["Ad", "sponsor"]
# list2 = ["cool", "neat", "ad", "great"]


# check =  any(item in list1 for item in list2)
# print(check)
# r = RSSParser()
# articles = r.parse_feed("https://kotaku.com/rss", "f70bd78d-71b0-4fae-9d15-9b321eb0fd75")
# articles = r.parse_feed("https://www.huffpost.com/section/front-page/feed", "42d45f8b-491b-432c-88bf-a78d9ae1b87b")

# a = ArticleFilter()
# new_a = a.filter(articles)
# print(len(new_a))
# print(articles[5])
# articles = r.articles("https://www.huffpost.com/section/front-page/feed", "42d45f8b-491b-432c-88bf-a78d9ae1b87b")

# articles = r.articles("https://www.newyorker.com/feed/everything", "d30d7c83-0ebc-44b7-8935-012d4125e5c7")



