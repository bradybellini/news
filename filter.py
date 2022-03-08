class ArticleFilter:

    filter_tags = ["ad", "advertisement", "sponsored", "sponsor"]

    def __init__(self) -> None:
        pass

    def _filter_tags(self, articles: list) -> list:
        clean__tagged_articles = []
        print(len(articles))
        for i in range(len(articles)):
            if articles[i]["tags"]:
                check = any(tag in articles[i]["tags"] for tag in self.filter_tags)
                if not check:
                    clean__tagged_articles.append(articles[i])
            else:
                clean__tagged_articles.append(articles[i])
        return clean__tagged_articles

    def filter(self, articles: list) -> list:
        tags = self._filter_tags(articles)
        return tags
