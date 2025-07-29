package main
import (
    "database/sql"
    _ "github.com/go-sql-driver/mysql"
    "os"
)
func main() {
    db, _ := sql.Open("mysql", "root:password@/test")
    user := os.Args[1]
    // VULNERABLE: unsanitized input
    db.Query("SELECT * FROM users WHERE name=" + user) // CWE-89
}
