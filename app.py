# from encodings import utf_8
# import string
# from webbrowser import get
# import feedparser, json, hashlib
# from supabase_test import insert_articles
from dotenv import load_dotenv
from flask import Flask, request
from celery import Celery

load_dotenv()
app = Flask(__name__)
app.config["CELERY_BROKER_URL"] = "redis://localhost:6379/0"
app.config["CELERY_RESULT_BACKEND"] = "redis://localhost:6379/0"

celery = Celery(app.name, broker=app.config["CELERY_BROKER_URL"])
celery.conf.update(app.config)


@app.route("/api/", methods=["POST"])
def get_feed():
    feed = request.args.get("feed", -1, type=str)
    feed_id = request.args.get("feedid", -1, type=str)
    # insert_articles(d)
    # return hashlib.md5(feed.encode()).hexdigest()
    bg_task_1(feed, feed_id)
    return feed

    # d = feedparser.parse(feed)
    # c = []


# # print(d.entries[1]['title'])
# for i in range(len(d.entries)):
#      c.append(d.entries[i].title)
# return jsonify(c)
# return jsonify([entries for entries in d.entries])


@celery.task
def bg_task_1(feed, feed_id):
    # insert_articles(feed, feed_id)
    pass



