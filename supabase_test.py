import os
import string
import feedparser
from dotenv import load_dotenv
from supabase import create_client, Client
from rssparser import RSSParser
import pprint

r = RSSParser()

r.articles('https://kotaku.com/rss')
def insert_articles(feed: string):

    load_dotenv()
    r = RSSParser()

    
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")

    supabase: Client = create_client(url, key)
    # for i in range(len(d.entries)):
    insert = supabase.table("article_test").insert(r.articles(feed)).execute()
    print(insert[0])
# d = feedparser.parse('https://kotaku.com/rss')


# # print(d.entries[1]['comments'])
# for i in range(len(d.entries)):
#     print(d.entries[i].guidislink)
insert_articles('https://kotaku.com/rss')