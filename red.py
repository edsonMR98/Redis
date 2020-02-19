import redis

r = redis.Redis(host='localhost', port=6379, db=0)
r.set('edson', 'test')
e = r.get('edson')
print(e.decode('ASCII'))