from rssparser import RSSParser
import pprint

r = RSSParser()
pp = pprint.PrettyPrinter(indent=2)

pp.pprint(r.articles('https://www.vg247.com/feed', '123')[1])