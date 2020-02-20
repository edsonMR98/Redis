# RedisPy

[Redis](https://redis.io/) is an open source (BSD licensed), in-memory data structure store, used as a database, cache and message broker.

This script was developed in order to test the redis-py package. This package is the Python interface to the Redis key-value store.

## Installing

- To run this script is needed to install the [redis-py](https://pypi.org/project/redis/) package.
- A running Redis server is required. See [Redis’s quickstart](https://redis.io/topics/quickstart) for installation instructions.
  - If you have Docker installed, you could create a container with the Redis official image executing `docker run --name redisContainer -p 6379:6379 -d redis`.
