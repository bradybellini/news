from encodings import utf_8
import string
from webbrowser import get
import feedparser, json, hashlib
from supabase_test import insert_articles
from flask import Flask, jsonify, request



app = Flask(__name__)


    
@app.route("/api/", methods=["POST"])
def get_feed():
    feed = request.args.get("feed", -1, type=str)
    # insert_articles(d)
    # return hashlib.md5(feed.encode()).hexdigest()
    return feed
    
    # d = feedparser.parse(feed)
    # c = []


# # print(d.entries[1]['title'])
    # for i in range(len(d.entries)):
    #      c.append(d.entries[i].title)
    # return jsonify(c)
    # return jsonify([entries for entries in d.entries])