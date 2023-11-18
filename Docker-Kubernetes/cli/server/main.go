package main

import (
	"fmt"
	"log"
	"net/http"
)

func home( w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "This is just a test page!")
	fmt.Println("Endpoint Hit: home")
	w.WriteHeader(http.StatusOK)
}

func main() {
	http.HandleFunc("/", home)
	log.Fatal(http.ListenAndServe(":10000", nil))
}