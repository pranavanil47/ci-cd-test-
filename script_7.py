# 4. Create vulnerable Docker application
dockerfile_content = '''# Vulnerable Dockerfile for Trivy testing
FROM ubuntu:18.04

# Vulnerable base image with known CVEs
LABEL maintainer="security-tester"
LABEL description="Intentionally vulnerable Docker image for Trivy SBOM/SCA testing"

# Install vulnerable system packages
RUN apt-get update && apt-get install -y \\
    curl=7.58.0-2ubuntu3.8 \\
    wget=1.19.4-1ubuntu2.2 \\
    openssl=1.1.1-1ubuntu2.1~18.04.15 \\
    libssl1.1=1.1.1-1ubuntu2.1~18.04.15 \\
    python3=3.6.7-1~18.04 \\
    python3-pip=9.0.1-2.3~ubuntu1.18.04.5 \\
    nodejs=8.10.0~dfsg-2ubuntu0.4 \\
    npm=3.5.2-0ubuntu4 \\
    openjdk-8-jdk=8u292-b10-0ubuntu1~18.04 \\
    mysql-client=5.7.36-0ubuntu0.18.04.1 \\
    git=1:2.17.1-1ubuntu0.12 \\
    vim=2:8.0.1453-1ubuntu1.8 \\
    apache2=2.4.29-1ubuntu4.21 \\
    nginx=1.14.0-0ubuntu1.9 \\
    && rm -rf /var/lib/apt/lists/*

# Create app directory
WORKDIR /app

# Copy vulnerable applications
COPY vulnerable-node-app/ ./node-app/
COPY vulnerable-python-app/ ./python-app/
COPY vulnerable-java-app/ ./java-app/

# Install Node.js vulnerable dependencies
WORKDIR /app/node-app
RUN npm install

# Install Python vulnerable dependencies
WORKDIR /app/python-app
RUN pip3 install -r requirements.txt

# Install Java dependencies (Maven not included, but pom.xml shows deps)
WORKDIR /app/java-app

# Create vulnerable startup script
WORKDIR /app
RUN echo '#!/bin/bash' > start.sh && \\
    echo 'echo "Starting vulnerable applications for Trivy testing..."' >> start.sh && \\
    echo 'echo "Node.js app available at port 3000"' >> start.sh && \\
    echo 'echo "Python app available at port 5000"' >> start.sh && \\
    echo 'echo "This container has intentionally vulnerable dependencies"' >> start.sh && \\
    echo 'cd /app/python-app && python3 app.py &' >> start.sh && \\
    echo 'cd /app/node-app && npm start &' >> start.sh && \\
    echo 'tail -f /dev/null' >> start.sh && \\
    chmod +x start.sh

# Expose vulnerable service ports
EXPOSE 3000 5000 8080

# Add vulnerable user with weak permissions
RUN useradd -m -s /bin/bash vulnuser && \\
    echo 'vulnuser:password123' | chpasswd && \\
    usermod -aG sudo vulnuser

# Set vulnerable file permissions
RUN chmod 777 /app && \\
    chmod 666 /etc/passwd

# Run as root (vulnerable practice)
USER root

CMD ["./start.sh"]
'''

with open("vulnerable-docker-app/Dockerfile", "w") as f:
    f.write(dockerfile_content)

print("Created Dockerfile with vulnerable configurations")