# Create comprehensive README files for each project
readme_content = '''# Vulnerable Applications for Trivy SBOM and SCA Testing

This collection contains intentionally vulnerable applications designed to test Trivy's Software Bill of Materials (SBOM) and Software Composition Analysis (SCA) capabilities.

## ⚠️ WARNING ⚠️
**These applications contain INTENTIONAL SECURITY VULNERABILITIES and should NEVER be deployed in production environments. They are designed solely for security testing purposes.**

## Projects Overview

### 1. Node.js Vulnerable Application (`vulnerable-node-app/`)
- **Language:** Node.js/JavaScript
- **Package Manager:** npm
- **Key Vulnerabilities:**
  - Express 4.16.0 - CVE-2022-24999
  - Lodash 4.17.11 - Prototype pollution
  - Moment 2.19.1 - ReDoS vulnerability
  - JWT 8.3.0 - Algorithm confusion CVE-2022-23529
  - Request 2.88.0 - Deprecated with security issues
  - And 15+ more vulnerable dependencies

### 2. Python Vulnerable Application (`vulnerable-python-app/`)
- **Language:** Python
- **Package Manager:** pip
- **Key Vulnerabilities:**
  - Django 1.11.0 - Multiple CVEs including SQL injection
  - Flask 0.12.2 - Multiple security issues
  - PyYAML 3.12 - CVE-2017-18342 arbitrary code execution
  - Pillow 5.2.0 - Multiple image processing CVEs
  - Cryptography 2.3 - Multiple cryptographic vulnerabilities
  - And 20+ more vulnerable dependencies

### 3. Java Vulnerable Application (`vulnerable-java-app/`)
- **Language:** Java
- **Build Tool:** Maven
- **Key Vulnerabilities:**
  - Log4j 2.14.1 - CVE-2021-44228 (Log4Shell)
  - Spring Framework 4.3.18 - CVE-2018-15756
  - Jackson 2.9.8 - Multiple deserialization CVEs
  - Commons Collections 3.2.1 - CVE-2015-6420
  - Struts 2.3.34 - Multiple RCE CVEs
  - And 15+ more vulnerable dependencies

### 4. Go Vulnerable Application (`vulnerable-go-app/`)
- **Language:** Go
- **Package Manager:** Go modules
- **Key Vulnerabilities:**
  - JWT-Go 3.2.0 - CVE-2020-26160
  - Gorilla WebSocket 1.4.0 - CVE-2020-27813
  - Gogo Protobuf 1.3.1 - CVE-2021-3121
  - Various golang.org/x packages with multiple CVEs
  - And 10+ more vulnerable dependencies

### 5. Docker Vulnerable Application (`vulnerable-docker-app/`)
- **Type:** Container Image
- **Base:** Ubuntu 18.04
- **Vulnerabilities:**
  - Vulnerable base OS packages
  - Insecure container configurations
  - Combines all above applications
  - Weak file permissions and user setup

## Testing with Trivy

### SBOM Generation
Generate Software Bill of Materials for each project:

```bash
# Node.js SBOM
cd vulnerable-node-app
trivy fs --format cyclonedx --output node-sbom.json .

# Python SBOM  
cd vulnerable-python-app
trivy fs --format cyclonedx --output python-sbom.json .

# Java SBOM
cd vulnerable-java-app  
trivy fs --format cyclonedx --output java-sbom.json .

# Go SBOM
cd vulnerable-go-app
trivy fs --format cyclonedx --output go-sbom.json .

# Docker SBOM
trivy image --format cyclonedx --output docker-sbom.json vulnerable-docker-app
```

### Software Composition Analysis (SCA)
Run vulnerability scanning on each project:

```bash
# Node.js SCA
cd vulnerable-node-app
trivy fs --security-checks vuln .

# Python SCA
cd vulnerable-python-app  
trivy fs --security-checks vuln .

# Java SCA
cd vulnerable-java-app
trivy fs --security-checks vuln .

# Go SCA
cd vulnerable-go-app
trivy fs --security-checks vuln .

# Docker SCA
trivy image vulnerable-docker-app
```

### Advanced Trivy Commands

```bash
# Generate detailed JSON report
trivy fs --format json --output detailed-report.json .

# Filter by severity
trivy fs --severity HIGH,CRITICAL .

# Show only unfixed vulnerabilities
trivy fs --ignore-unfixed .

# Generate SARIF format for CI/CD integration
trivy fs --format sarif --output results.sarif .
```

## Expected Results

When running Trivy on these applications, you should expect to find:

- **100+ total vulnerabilities** across all projects
- **Multiple CRITICAL severity findings** including Log4Shell, prototype pollution, and RCE vulnerabilities
- **Comprehensive SBOM data** showing all dependencies and their relationships
- **License information** for all packages
- **Detailed CVE mappings** with CVSS scores and descriptions

## Installation Instructions

### Node.js Application
```bash
cd vulnerable-node-app
npm install
npm start  # Runs on port 3000
```

### Python Application
```bash
cd vulnerable-python-app
pip install -r requirements.txt
python app.py  # Runs on port 5000
```

### Java Application
```bash
cd vulnerable-java-app
mvn compile  # Compiles and downloads dependencies
```

### Go Application
```bash
cd vulnerable-go-app
go mod download
go run main.go  # Runs on port 8080
```

### Docker Application
```bash
cd vulnerable-docker-app
docker build -t vulnerable-app .
docker run -p 3000:3000 -p 5000:5000 -p 8080:8080 vulnerable-app
```

## Security Testing Use Cases

These applications are perfect for:

- **Testing SAST/SCA tools** like Trivy, Snyk, OWASP Dependency Check
- **CI/CD pipeline security integration** testing
- **Security training and education** scenarios
- **Vulnerability management process** validation
- **SBOM tooling evaluation** and comparison
- **Compliance reporting** testing (NIST, SPDX, CycloneDX)

## Legal Notice

These applications are provided for educational and testing purposes only. The maintainers are not responsible for any misuse of these vulnerable applications. Use only in controlled, isolated environments.

## Contributing

When adding new vulnerable dependencies:
1. Ensure they have known CVE entries
2. Use versions with confirmed vulnerabilities
3. Update documentation with CVE details
4. Test with Trivy to confirm detection

## License

MIT License - See LICENSE file for details.

---

**Remember: These are INTENTIONALLY VULNERABLE applications. Never use in production!**
'''

with open("README.md", "w") as f:
    f.write(readme_content)

print("Created comprehensive README.md")