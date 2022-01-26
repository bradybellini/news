import os
import feedparser
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()
d = feedparser.parse("https://kotaku.com/rss")
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)
# for i in range(len(d.entries)):
#     supabase.table("article_test").insert(
#         {
#             "title": d.entries[i]["title"],
#             "author": d.entries[i]["author"],
#             "link": d.entries[i]["link"],
#             "summary": d.entries[i]["summary"],
#             "published": d.entries[i]["published"],
#         }
#     ).execute()

# d = feedparser.parse('https://kotaku.com/rss')


print(d.entries[1]['comments'])
# for i in range(len(d.entries)):
#     print(d.entries[i].published)
