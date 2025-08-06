# 5. Create vulnerable Go application
go_mod_content = '''module vulnerable-go-app

go 1.16

require (
    github.com/gin-gonic/gin v1.7.0 // Multiple CVEs
    github.com/gorilla/websocket v1.4.0 // CVE-2020-27813
    github.com/dgrijalva/jwt-go v3.2.0+incompatible // CVE-2020-26160
    github.com/go-sql-driver/mysql v1.5.0 // Multiple CVEs
    github.com/lib/pq v1.8.0 // SQL injection potential
    golang.org/x/crypto v0.0.0-20200622213623-75b288015ac9 // Multiple CVEs
    golang.org/x/net v0.0.0-20200625001655-4c5254603344 // Multiple CVEs
    gopkg.in/yaml.v2 v2.3.0 // Billion laughs attack
    github.com/gogo/protobuf v1.3.1 // CVE-2021-3121
    github.com/hashicorp/consul/api v1.7.0 // Multiple CVEs
    github.com/docker/docker v17.12.0-ce-rc1.0.20200916142827-bd33bbf0497b+incompatible // Multiple CVEs
    github.com/kubernetes/kubernetes v1.18.0 // Multiple CVEs
    github.com/prometheus/client_golang v1.7.0 // DoS vulnerabilities
    github.com/sirupsen/logrus v1.6.0 // Log injection potential
    github.com/spf13/viper v1.7.0 // Path traversal potential
)
'''

with open("vulnerable-go-app/go.mod", "w") as f:
    f.write(go_mod_content)

print("Created go.mod with vulnerable Go dependencies")