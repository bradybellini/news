from flair.data import Sentence
from flair.models import SequenceTagger
from flair.models import TextClassifier
import json

test_article = {
    "feed_id": "f70bd78d-71b0-4fae-9d15-9b321eb0fd75",
    "title": "Be Prepared For These 7 Big Overwatch 2 Gameplay Changes",
    "link": "https://kotaku.com/overwatch-2-release-time-blizzard-gameplay-changes-tips-1849615186",
    "author": "Ashley Bardhan",
    "published": "2022-10-04 18:20:00",
    "summary": "Sorry, the old Overwatch can’t come to the phone right now. She’s dead. Today, October 4 at 3 p.m. EST, Overwatch 2 will come to replace her, and the sun has long  set on days of 6v6 and free-range characters not cloistered behind a battle pass.Read more...",
    "guid": "1849615186",
    "uid": "98bb1609d2d6ca07e686158624f75c3d",
    "tags": [
        "overwatch",
        "dva",
        "sombra",
        "transmediastorytelling",
        "crouch",
        "videogamecharacters",
        "multiplayeronlinegames",
        "blizzardentertainment",
        "sports",
        "mercy",
        "multiplayervideogames",
        "brigitte",
        "fictionalcharacters",
        "fiction",
    ],
    "Entities": [
        {
            "Word": "Bridgewater",
            "Classification": "ORG",
            "Start Position": 0,
            "End Position": 11,
        },
        {
            "Word": "Ray Dalio",
            "Classification": "PER",
            "Start Position": 20,
            "End Position": 29,
        },
    ],
    "Sentiment": {"Score": 0.9848532676696777, "Tag": "NEGATIVE"},
}



# print(json.dumps(test_article).encode('utf-8'))
# print(test_article["Entities"])
# classifier = TextClassifier.load("sentiment")
sentence = Sentence(
    "Every U.S. PlayStation 2 Game Manual Is Now Scanned In 4K"
)
# classifier.predict(sentence)

# sent = {"Score": sentence.score, "Tag": sentence.tag}
# test_article["Sentiment"] = sent
# print(test_article)
# print(sentence.score)
# print(sentence.tag)
# print(sentence.text)


tagger = SequenceTagger.load("ner-large")

# result = tagger.predict(sentence)
# print(result)
ents = [
    {
        "Word": entity.text,
        "Classification": entity.tag,
        "Start Position": entity.start_position,
        "End Position": entity.end_position,
    }
    for entity in sentence.get_spans("ner")
]
print(ents)
    
# ents = [
#     {
#         "Word": entity.text,
#         "Classification": entity.tag,
#         "Start Position": entity.start_position,
#         "End Position": entity.end_position,
#     }
# ]
# print(ents)

# test_article["Entities"] = ents
# print(test_article)
# for entity in sentence.get_spans('ner'):
#     print(entity.text)
#     print(entity.end_position)
#     print(entity.tag)
# spacy.require_cpu()
# nlp = en_core_web_trf.load(disable=["tagger", "parser", "attribute_ruler", "lemmatizer"])
# nlp.add_pipe('opentapioca')
# ner = spacy.load("en_core_web_trf", disable=["tagger", "parser", "attribute_ruler", "lemmatizer"] )
# raw_text="Brazilian President Jair Bolsonaro Gets Second Shot at Re-Election"
# doc = nlp(test_article["title"])
# ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
# ents = [{'Word': e.text, 'Classification': e.label_} for e in doc.ents]


# print(ents)

# for ent in doc.ents:
#     print(ent.text, ent.start_char, ent.end_char, ent.label_)

# list1 = ["Ad", "sponsor"]
# list2 = ["cool", "neat", "ad", "great"]


# check =  any(item in list1 for item in list2)
# print(check)
# r = rssparser.RSSParser()
# articles = r.parse_feed(
#     "https://kotaku.com/rss", "f70bd78d-71b0-4fae-9d15-9b321eb0fd75"
# )
# articles = r.parse_feed("https://www.huffpost.com/section/front-page/feed", "42d45f8b-491b-432c-88bf-a78d9ae1b87b")
# print(articles[2])
# a = ArticleFilter()
# new_a = a.filter(articles)
# print(len(new_a))
# print(articles[5])
# articles = r.articles("https://www.huffpost.com/section/front-page/feed", "42d45f8b-491b-432c-88bf-a78d9ae1b87b")

# articles = r.articles("https://www.newyorker.com/feed/everything", "d30d7c83-0ebc-44b7-8935-012d4125e5c7")


# test_article = {
#     "feed_id": "f70bd78d-71b0-4fae-9d15-9b321eb0fd75",
#     "title": "Be Prepared For These 7 Big Overwatch 2 Gameplay Changes",
#     "link": "https://kotaku.com/overwatch-2-release-time-blizzard-gameplay-changes-tips-1849615186",
#     "author": "Ashley Bardhan",
#     "published": "2022-10-04 18:20:00",
#     "summary": "Sorry, the old Overwatch can’t come to the phone right now. She’s dead. Today, October 4 at 3 p.m. EST, Overwatch 2 will come to replace her, and the sun has long  set on days of 6v6 and free-range characters not cloistered behind a battle pass.Read more...",
#     "guid": "1849615186",
#     "uid": "98bb1609d2d6ca07e686158624f75c3d",
#     "tags": [
#         "overwatch",
#         "dva",
#         "sombra",
#         "transmediastorytelling",
#         "crouch",
#         "videogamecharacters",
#         "multiplayeronlinegames",
#         "blizzardentertainment",
#         "sports",
#         "mercy",
#         "multiplayervideogames",
#         "brigitte",
#         "fictionalcharacters",
#         "fiction",
#     ],
# }
