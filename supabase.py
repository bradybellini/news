import os
from dotenv import load_dotenv
from supabase import create_client, Client
from rssparser import RSSParser


class supa:
    def __init__(self) -> None:
        load_dotenv()
        self.url: str = os.environ.get("SUPABASE_URL")
        self.key: str = os.environ.get("SUPABASE_KEY")
        self.r = RSSParser()

    def _create_client(self):
        return create_client(self.url, self.key)

    def insert():
        pass
