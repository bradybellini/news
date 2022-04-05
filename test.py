from supapsql import SupaPSQL
from rssparser import RSSParser
from filter import ArticleFilter
import spacy
from spacy import displacy


spacy.require_cpu()
ner = spacy.load("en_core_web_sm", disable=["tagger", "parser", "attribute_ruler", "lemmatizer"] )
raw_text="How SiriusXM Bought and Bungled a Beloved Podcast Network"
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



