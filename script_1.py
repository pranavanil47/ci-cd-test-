# 1. Create vulnerable Node.js application
package_json = {
    "name": "vulnerable-node-demo",
    "version": "1.0.0",
    "description": "Intentionally vulnerable Node.js app for Trivy testing",
    "main": "app.js",
    "scripts": {
        "start": "node app.js",
        "test": "echo \"Error: no test specified\" && exit 1"
    },
    "dependencies": {
        "express": "4.16.0",  # CVE-2022-24999
        "lodash": "4.17.11",  # Multiple CVEs
        "jquery": "3.4.0",    # XSS vulnerabilities
        "moment": "2.19.1",   # ReDoS vulnerability
        "debug": "2.6.8",     # CVE-2017-20165
        "handlebars": "4.0.12", # Multiple template injection CVEs
        "ejs": "2.5.7",       # Code injection CVE-2017-1000188
        "serialize-javascript": "1.4.0", # XSS CVE-2019-16769
        "axios": "0.18.0",    # Server-side request forgery
        "validator": "10.8.0", # Multiple validation bypass CVEs
        "morgan": "1.9.0",    # Potential log injection
        "cookie-parser": "1.4.3", # Potential cookie manipulation
        "helmet": "3.12.0",   # Outdated security headers
        "cors": "2.8.4",      # CORS misconfiguration potential
        "multer": "1.3.0",    # File upload vulnerabilities
        "jsonwebtoken": "8.3.0", # JWT algorithm confusion CVE-2022-23529
        "bcrypt": "2.0.0",    # Potential timing attacks
        "mongoose": "5.2.0",  # NoSQL injection potential
        "socket.io": "2.1.0", # Multiple XSS and DoS CVEs
        "request": "2.88.0"   # Deprecated with security issues
    },
    "devDependencies": {
        "nodemon": "1.18.0",  # Command injection potential
        "webpack": "4.28.0",  # Multiple CVEs including path traversal
        "babel-core": "6.26.0" # Prototype pollution
    },
    "keywords": ["vulnerable", "security", "testing", "trivy"],
    "author": "Security Tester",
    "license": "MIT"
}

with open("vulnerable-node-app/package.json", "w") as f:
    json.dump(package_json, f, indent=2)

print("Created package.json with vulnerable dependencies")