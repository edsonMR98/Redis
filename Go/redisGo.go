package main

import (
	"encoding/json"
	"fmt"

	"github.com/go-redis/redis"
)

// ENP define the struct of each event not persisted
type ENP struct {
	Question int
	Prop     int
	User     int
}

func main() {
	client := redis.NewClient(&redis.Options{
		Addr:     "localhost:6379",
		Password: "", // no password set
		DB:       0,  // use default DB
	})

	err := client.Set("edson", "test", 0).Err() // Sets 'test' value to 'edson' key
	if err != nil {
		panic(err)
	}
	e, err := client.Get("edson").Result() // Gets the value of 'edson' key
	if err != nil {
		panic(err)
	}
	fmt.Println("edson:", e)

	err = client.MSet("Mexico", "CDMX", "Croatia", "Zagreb").Err() // Multi-set
	if err != nil {
		panic(err)
	}
	c, err := client.Get("Croatia").Result()
	if err != nil {
		panic(err)
	}
	fmt.Println("Croatia:", c)

	// Redis list
	event, _ := json.Marshal(ENP{Question: 1, Prop: 1, User: 1}) // Defines a ENP "object" and then it is converted to JSON encode (bytes)
	client.RPush("eventsNotPersisted", string(event))            // Adds a values to the tail of 'eventsNotPersisted' list
	event, _ = json.Marshal(ENP{Question: 2, Prop: 2, User: 2})
	client.RPush("eventsNotPersisted", string(event))
	event, _ = json.Marshal(ENP{Question: 3, Prop: 3, User: 3})
	client.RPush("eventsNotPersisted", string(event))

	len, _ := client.LLen("eventsNotPersisted").Result() // Gets the length of a list (int64 type)
	for x := 0; x < int(len); x++ {                      // Converts int64 to int
		event, err := client.LPop("eventsNotPersisted").Result() // Removes the element and return it
		if err != nil {
			panic(err)
		}
		var enp ENP                         // ENP "object"
		json.Unmarshal([]byte(event), &enp) // Unmarshal JSON to ENP struct
		fmt.Println("Question", enp.Question)
	}
}
