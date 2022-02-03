
from feedparser import parse
from lxml import html
from lxml.html.clean import clean_html
import hashlib



class RSSParser:
    def __init__(self) -> None:
        pass

    def _get_article_info(self, feed_id: str, article: dict) -> dict:
        authors = getattr(article, "author", "no authors listed")
        summary = getattr(article, "summary", "none")
        if summary != 'none':
            summary = clean_html(html.fromstring(summary)).text_content().strip()
            
        return {
            "feed_id": feed_id,
            "title": article.title,
            "link": article.link,
            "author": authors,
            "published": article.published,
            "summary": summary,
            "guid": article.link if article.guidislink else article.guid,
            "uid": hashlib.md5(str(article.title + article.link).encode()).hexdigest(),
        }
    
    def articles(self, feed, feed_id):
        parsed = parse(feed)
        articles = [parsed for parsed in parsed.entries]
        return [self._get_article_info(feed_id, entry) for entry in articles]
