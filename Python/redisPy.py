import redis
import json

client = redis.Redis(host='localhost', port=6379, db=0) # Redis client

client.set('edson', 'test') # Sets 'test' value to 'edson' key
e = client.get('edson') # Gets the value of 'edson' key
print(e.decode('ASCII')) # Decodes to string

client.mset({"Mexico": "CDMX", "Croatia": "Zagreb"}) # Multi-set
c = client.get("Croatia")
print(c.decode('ASCII'))

# Redis lists
client.rpush('eventsNotPersisted', str({"question": 1, "prop": 1, "user": 1})) # Adds a values to the tail of 'eventsNotPersisted' list
client.rpush('eventsNotPersisted', str({"question": 2, "prop": 2, "user": 2}))
client.rpush('eventsNotPersisted', str({'question': 3, 'prop': 3, 'user': 3}))

print("List len:", client.llen('eventsNotPersisted')) # Gets the length of a list
for _ in range(0, client.llen('eventsNotPersisted')):
    e = client.lpop('eventsNotPersisted') # Remove the element and return it
    eStr = e.decode('ASCII')
    eDict = json.loads(e.decode('ASCII').replace("'", '"'))
    print("Question", eDict["question"])