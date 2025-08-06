# Create Go application source code
go_app_content = '''package main

import (
    "fmt"
    "net/http"
    "log"
    "encoding/json"
    "database/sql"
    "crypto/md5"
    "gopkg.in/yaml.v2"
    
    "github.com/gin-gonic/gin"
    "github.com/dgrijalva/jwt-go"
    "github.com/gorilla/websocket"
    _ "github.com/go-sql-driver/mysql"
    "github.com/sirupsen/logrus"
    "github.com/gogo/protobuf/proto"
)

// Vulnerable JWT secret
var jwtSecret = []byte("insecure-secret")

// Vulnerable WebSocket upgrader with no origin checking
var upgrader = websocket.Upgrader{
    CheckOrigin: func(r *http.Request) bool {
        return true // Vulnerable: allows any origin
    },
}

// Vulnerable struct for demonstration
type VulnerableUser struct {
    ID       int    \`json:"id"\`
    Username string \`json:"username"\`
    Password string \`json:"password"\` // Plain text password storage
    Email    string \`json:"email"\`
}

func main() {
    // Initialize vulnerable Gin router
    gin.SetMode(gin.DebugMode) // Vulnerable: debug mode in production
    router := gin.Default()
    
    // Configure vulnerable logging
    logrus.SetLevel(logrus.DebugLevel)
    
    fmt.Println("Starting vulnerable Go application for Trivy testing...")
    fmt.Println("This app contains intentionally vulnerable dependencies")
    
    // Define vulnerable routes
    router.GET("/", homeHandler)
    router.POST("/login", loginHandler)
    router.GET("/yaml", yamlHandler)
    router.GET("/sql", sqlHandler)
    router.GET("/ws", websocketHandler)
    router.GET("/hash", hashHandler)
    router.POST("/proto", protoHandler)
    
    // Start server on vulnerable configuration
    log.Fatal(router.Run(":8080")) // No TLS, default timeouts
}

func homeHandler(c *gin.Context) {
    vulnerabilities := []string{
        "Gin 1.7.0 - Multiple CVEs",
        "JWT-Go 3.2.0 - CVE-2020-26160",
        "Gorilla WebSocket 1.4.0 - CVE-2020-27813", 
        "MySQL Driver 1.5.0 - Multiple CVEs",
        "Golang.org/x/crypto - Multiple CVEs",
        "Golang.org/x/net - Multiple CVEs",
        "YAML v2.3.0 - Billion laughs attack",
        "Gogo Protobuf 1.3.1 - CVE-2021-3121",
        "And many more vulnerable dependencies...",
    }
    
    c.JSON(http.StatusOK, gin.H{
        "message": "Vulnerable Go app for Trivy SBOM and SCA testing",
        "vulnerabilities": vulnerabilities,
        "endpoints": []string{
            "/login - JWT vulnerabilities",
            "/yaml - YAML parsing vulnerabilities", 
            "/sql - SQL injection demo",
            "/ws - WebSocket vulnerabilities",
            "/hash - Weak hashing demo",
            "/proto - Protobuf vulnerabilities",
        },
    })
}

func loginHandler(c *gin.Context) {
    var user VulnerableUser
    if err := c.ShouldBindJSON(&user); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    
    // Vulnerable JWT creation with algorithm confusion risk
    token := jwt.NewWithClaims(jwt.SigningMethodHS256, jwt.MapClaims{
        "user": user.Username,
        "admin": false,
    })
    
    // Sign token with vulnerable library
    tokenString, err := token.SignedString(jwtSecret)
    if err != nil {
        c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to generate token"})
        return
    }
    
    c.JSON(http.StatusOK, gin.H{
        "token": tokenString,
        "warning": "Vulnerable JWT implementation used",
        "user": user, // Exposes user data including password
    })
}

func yamlHandler(c *gin.Context) {
    yamlData := c.Query("data")
    if yamlData == "" {
        c.JSON(http.StatusBadRequest, gin.H{"error": "No YAML data provided"})
        return
    }
    
    // Vulnerable YAML parsing - billion laughs attack possible
    var result interface{}
    err := yaml.Unmarshal([]byte(yamlData), &result)
    if err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    
    c.JSON(http.StatusOK, gin.H{
        "parsed": result,
        "warning": "Vulnerable YAML parsing with DoS risk",
    })
}

func sqlHandler(c *gin.Context) {
    userID := c.Query("id")
    if userID == "" {
        userID = "1"
    }
    
    // Vulnerable SQL query construction
    query := fmt.Sprintf("SELECT * FROM users WHERE id = %s", userID)
    
    // Simulate database connection with vulnerable MySQL driver
    db, err := sql.Open("mysql", "user:pass@tcp(localhost:3306)/testdb")
    if err != nil {
        logrus.Error("Database connection failed: ", err)
    }
    defer db.Close()
    
    c.JSON(http.StatusOK, gin.H{
        "query": query,
        "warning": "Vulnerable SQL query with injection risk",
        "error": "Database connection simulated",
    })
}

func websocketHandler(c *gin.Context) {
    // Vulnerable WebSocket upgrade without origin validation
    conn, err := upgrader.Upgrade(c.Writer, c.Request, nil)
    if err != nil {
        logrus.Error("WebSocket upgrade failed: ", err)
        return
    }
    defer conn.Close()
    
    // Echo messages back (vulnerable to XSS if used in web context)
    for {
        messageType, message, err := conn.ReadMessage()
        if err != nil {
            logrus.Error("WebSocket read error: ", err)
            break
        }
        
        // Echo back without sanitization
        err = conn.WriteMessage(messageType, message)
        if err != nil {
            logrus.Error("WebSocket write error: ", err)
            break
        }
    }
}

func hashHandler(c *gin.Context) {
    data := c.Query("data")
    if data == "" {
        c.JSON(http.StatusBadRequest, gin.H{"error": "No data provided"})
        return
    }
    
    // Vulnerable: using MD5 for hashing (cryptographically broken)
    hash := md5.Sum([]byte(data))
    
    c.JSON(http.StatusOK, gin.H{
        "data": data,
        "md5_hash": fmt.Sprintf("%x", hash),
        "warning": "MD5 is cryptographically broken",
    })
}

func protoHandler(c *gin.Context) {
    // Simulate vulnerable protobuf handling
    data, err := c.GetRawData()
    if err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    
    // Vulnerable protobuf unmarshaling (CVE-2021-3121 in gogo/protobuf)
    var message proto.Message
    _ = message // Placeholder for vulnerable protobuf operations
    
    c.JSON(http.StatusOK, gin.H{
        "message": "Protobuf data processed",
        "size": len(data),
        "warning": "Vulnerable gogo/protobuf library used (CVE-2021-3121)",
    })
}
'''

with open("vulnerable-go-app/main.go", "w") as f:
    f.write(go_app_content)

print("Created main.go for Go vulnerable application")