# Let me create multiple vulnerable projects for testing Trivy SBOM and SCA

import os
import json

# Create directories for different project types
os.makedirs("vulnerable-node-app", exist_ok=True)
os.makedirs("vulnerable-python-app", exist_ok=True)
os.makedirs("vulnerable-java-app", exist_ok=True)
os.makedirs("vulnerable-docker-app", exist_ok=True)
os.makedirs("vulnerable-go-app", exist_ok=True)

print("Created project directories successfully")