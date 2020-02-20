import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0)

r.set('edson', 'test')
e = r.get('edson')
print(e.decode('ASCII'))

r.mset({"Mexico": "CDMX", "Croatia": "Zagreb"})
c = r.get("Croatia")
print(c.decode('ASCII'))

# Redis lists
r.rpush('eventsNotPersisted', str({"question": 1, "prop": 1, "user": 1}))
r.rpush('eventsNotPersisted', str({"question": 2, "prop": 2, "user": 2}))
r.rpush('eventsNotPersisted', str({'question': 3, 'prop': 3, 'user': 3}))

print("List len:", r.llen('eventsNotPersisted'))
for _ in range(0, r.llen('eventsNotPersisted')):
    e = r.lpop('eventsNotPersisted')
    eStr = e.decode('ASCII')
    eDict = json.loads(e.decode('ASCII').replace("'", '"'))
    print("Question", eDict["question"])