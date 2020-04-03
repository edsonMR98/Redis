# Redis

[Redis](https://redis.io/) is an open source (BSD licensed), in-memory data structure store, used as a database, cache and message broker.

This script was developed in order to test the redis package.

## Prerequisites

A running Redis server is required. See [Redis’s quickstart](https://redis.io/topics/quickstart) for installation instructions.
If you have Docker installed, you could create a container with the Redis official image executing docker run --name redisContainer -p 6379:6379 -d redis.

## Python

redis-py is the Python interface to the Redis key-value store.

### Execution

- To run this script you need to install the [redis-py](https://pypi.org/project/redis/) package.

## Go

[redis-go](https://godoc.org/github.com/go-redis/redis) package implements a Redis client. It is the Redis client for Go.

### Execution

 - Make sure to follow the installation instructions of [go-redis](https://github.com/go-redis/redis).
