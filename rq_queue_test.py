import queue
from redis import Redis
from rq import Queue


q = Queue(connection=Redis('127.0.0.1',6379))

from rq_test import count_words_at_url

result = q.enqueue(count_words_at_url, 'https://bradybellin.com')


print(result)