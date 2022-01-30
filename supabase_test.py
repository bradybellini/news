import os
import string
import feedparser
from dotenv import load_dotenv
from supabase import create_client, Client
from rssparser import RSSParser
import pprint

# r = RSSParser()

# r.articles('https://kotaku.com/rss', '559b67c6-90af-4ce9-91f1-74fbedff7d00')
def insert_articles(feed: string, feed_id):

    load_dotenv()
    r = RSSParser()

    
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")

    supabase: Client = create_client(url, key)
    # for i in range(len(d.entries)):
    insert = supabase.table("articles_duplicate").upsert(r.articles(feed, feed_id) ).execute()
    print(insert[0])
# d = feedparser.parse('https://kotaku.com/rss')


# # print(d.entries[1]['comments'])
# for i in range(len(d.entries)):
#     print(d.entries[i].guidislink)
insert_articles('https://kotaku.com/rss', '559b67c6-90af-4ce9-91f1-74fbedff7d00')