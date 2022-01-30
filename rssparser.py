
import feedparser
import hashlib


class RSSParser:
    def __init__(self) -> None:
        pass

    # double check author and tags if they return a list
    def _get_article_info(self, feed_id: str, article: dict) -> dict:
        authors = getattr(article, "author", "no authors listed")
        return {
            "feed_id": feed_id,
            "title": article.title,
            "link": article.link,
            # "author": authors,
            "published": article.published,
            "summary": getattr(article, "summary", "none"),
            "guid": article.link if article.guidislink else article.guid,
            "uid": hashlib.md5(str(article.title + article.link).encode()).hexdigest(),
        }
    
    def articles(self, feed, feed_id):
        parsed = feedparser.parse(feed)
        articles = [parsed for parsed in parsed.entries]
        return [self._get_article_info(feed_id, entry) for entry in articles]
