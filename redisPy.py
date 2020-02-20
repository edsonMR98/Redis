import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0) # Redis client

r.set('edson', 'test') # Sets 'test' value to 'edson' key
e = r.get('edson') # Gets the value of 'edson' key
print(e.decode('ASCII')) # Decodes to string

r.mset({"Mexico": "CDMX", "Croatia": "Zagreb"}) # Multi-set
c = r.get("Croatia")
print(c.decode('ASCII'))

# Redis lists
r.rpush('eventsNotPersisted', str({"question": 1, "prop": 1, "user": 1})) # Adds a values to the tail of 'eventsNotPersisted' list
r.rpush('eventsNotPersisted', str({"question": 2, "prop": 2, "user": 2}))
r.rpush('eventsNotPersisted', str({'question': 3, 'prop': 3, 'user': 3}))

print("List len:", r.llen('eventsNotPersisted')) # Gets the length of a list
for _ in range(0, r.llen('eventsNotPersisted')):
    e = r.lpop('eventsNotPersisted') # Remove the element and return it
    eStr = e.decode('ASCII')
    eDict = json.loads(e.decode('ASCII').replace("'", '"'))
    print("Question", eDict["question"])