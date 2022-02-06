import os
from dotenv import load_dotenv
from supainsert import create_client, Client
from rssparser import RSSParser


class SupaInsert:
    def __init__(self, table: str) -> None:
        load_dotenv()
        self.url: str = os.environ.get("SUPABASE_URL")
        self.key: str = os.environ.get("SUPABASE_KEY")
        self.table = table

    def _create_client(self) -> Client:
        supabase: Client = create_client(self.url, self.key)
        return supabase

    def insert(self, feed: str, feed_id: str):
        r = RSSParser(feed, feed_id)
        
    def select(self):
        pass

