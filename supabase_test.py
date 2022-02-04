import os
import string
from dotenv import load_dotenv
from supabase import create_client, Client
from rssparser import RSSParser

# r = RSSParser()

# r.articles('https://kotaku.com/rss', '559b67c6-90af-4ce9-91f1-74fbedff7d00')
def insert_articles(feed: string, feed_id):

    load_dotenv()
    r = RSSParser()

    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")

    supabase: Client = create_client(url, key)
    # for i in range(len(d.entries)):
    # insert = supabase.table("articles_duplicate").upsert(r.articles(feed, feed_id) ).execute()
    # print(insert[0])
    select = supabase.table("feeds").select('feed_url','id').execute()
    # print(len(select[0]))
    for i in range(len(select[0])):
        insert = supabase.table("articles_duplicate").upsert(r.articles(select[0][i]['feed_url'], select[0][i]['id']) ).execute()
        print(insert)
    # d = feedparser.parse('https://kotaku.com/rss')
    # tree = html.fromstring(select[0][1]["summary"])
    # print(clean_html(tree).text_content().strip())
    # articles = r.articles(feed, feed_id)
    # print(articles[0]['summary'])

# # print(d.entries[1]['comments'])
# for i in range(len(d.entries)):
#     print(d.entries[i].guidislink)
# insert_articles("https://kotaku.com/rss", "559b67c6-90af-4ce9-91f1-74fbedff7d00")
