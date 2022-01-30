from rssparser import RSSParser
import pprint

r = RSSParser()
pp = pprint.PrettyPrinter(indent=2)

pp.pprint(r.articles('https://kotaku.com/rss')[1])