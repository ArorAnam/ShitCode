package main

import (
	"fmt"
	"net/http"

	"github.com/google/uuid"
	"github.com/gorilla/mux"
)

func router() {
	r := mux.NewRouter()
	r.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		id := uuid.New()
		fmt.Fprintf(w, "Generated UUID: %s", id)
	})
	http.ListenAndServe(":8080", r)
}
