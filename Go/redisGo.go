package main

import (
	"fmt"

	"github.com/go-redis/redis"
)

func main() {
	client := redis.NewClient(&redis.Options{
		Addr:     "localhost:6379",
		Password: "", // no password set
		DB:       0,  // use default DB
	})

	err := client.Set("edson", "test", 0).Err()
	if err != nil {
		panic(err)
	}

	e, err := client.Get("edson").Result()
	if err != nil {
		panic(err)
	}
	fmt.Println("edson:", e)

	err = client.MSet("Mexico", "CDMX", "Croatia", "Zagreb").Err()
	if err != nil {
		panic(err)
	}
	c, err := client.Get("Croatia").Result()
	if err != nil {
		panic(err)
	}
	fmt.Println("Croatia:", c)
}
