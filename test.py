import spacy
import en_core_web_trf

spacy.require_cpu()
nlp = en_core_web_trf.load(disable=["tagger", "parser", "attribute_ruler", "lemmatizer"])
nlp.add_pipe('opentapioca')
# ner = spacy.load("en_core_web_trf", disable=["tagger", "parser", "attribute_ruler", "lemmatizer"] )
raw_text="Stadia controllers could become e-waste unless Google issues Bluetooth update"
doc = nlp(raw_text)
# ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
ents = [(e.text, e.kb_id_, e.label_, e._.description, e._.score) for e in doc.ents]


print(ents)

# for ent in doc.ents:
#     print(ent.text, ent.start_char, ent.end_char, ent.label_)

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



