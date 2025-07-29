package main
import (
    "io/ioutil"
    "net/http"
)
func handler(w http.ResponseWriter, r *http.Request) {
    file := r.URL.Query().Get("file")
    // VULNERABLE: reads arbitrary file path
    data, _ := ioutil.ReadFile("/var/www/" + file) // CWE-22
    w.Write(data)
}
