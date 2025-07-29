package main
import (
    "os/exec"
    "os"
)
func main() {
    arg := os.Args[1]
    // VULNERABLE: unsanitized command execution
    exec.Command("sh", "-c", "ls "+arg).Run() // CWE-78
}
