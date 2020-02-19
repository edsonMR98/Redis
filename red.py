import redis

r = redis.Redis(host='localhost', port=6379, db=0)

r.set('events', 'test')
e = r.get('edson')
print(e.decode('ASCII'))

r.mset({"Mexico": "CDMX", "Croatia": "Zagreb"})
c = r.get("Croatia")
print(c.decode('ASCII'))