import feedparser
import hashlib


class RSSParser:
    def __init__(self) -> None:
        pass

    # double check author and tags if they return a list
    def _get_article_info(self, feed: str, article: dict) -> dict:
        # tags = getattr(article, "tags", "none")
        authors = getattr(article, "authors", "no authors listed")
        guid = article.link if article.guidislink else article.guid
        return {
            "title": article.title,
            "link": article.link,
            "author": authors,
            # "tags": tags,
            "published": article.published,
            "summary": article.summary,
            # "guid": guid,
            # "uid": hashlib.md5(str(article.title + article.link).encode()).hexdigest(),
        }
    
    def articles(self, feed):
        parsed = feedparser.parse(feed)
        articles = [parsed for parsed in parsed.entries]
        return [self._get_article_info(parsed.feed, entry) for entry in articles]
