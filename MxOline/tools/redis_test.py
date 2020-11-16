import redis

r = redis.Redis(host='localhost', port=6379, db=0, charset='utf8', decode_responses=True)

r.set('mobile','18869095465')
r.expire('mobile',1)
import time
time.sleep(2)
print(r.get('mobile'))

