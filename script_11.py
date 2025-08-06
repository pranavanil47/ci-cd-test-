# Create a comprehensive Trivy testing script
trivy_test_script = '''#!/bin/bash

# Trivy SBOM and SCA Testing Script
# This script tests all vulnerable applications with various Trivy commands

echo "🔍 Trivy SBOM and SCA Testing Script"
echo "======================================"
echo "Testing vulnerable applications with Trivy"
echo "⚠️  WARNING: These are intentionally vulnerable applications!"
echo ""

# Create results directory
mkdir -p trivy-results
cd trivy-results

echo "📦 Testing Node.js Application..."
echo "--------------------------------"
cd ../vulnerable-node-app

# SBOM Generation
echo "Generating SBOM (CycloneDX format)..."
trivy fs --format cyclonedx --output ../trivy-results/node-sbom.json .

echo "Generating SBOM (SPDX format)..."  
trivy fs --format spdx-json --output ../trivy-results/node-sbom-spdx.json .

# SCA Scanning
echo "Running SCA scan..."
trivy fs --format json --output ../trivy-results/node-sca.json .

echo "Running high/critical vulnerability scan..."
trivy fs --severity HIGH,CRITICAL --format table --output ../trivy-results/node-critical.txt .

echo ""
echo "🐍 Testing Python Application..."
echo "-------------------------------"
cd ../vulnerable-python-app

# SBOM Generation  
echo "Generating SBOM (CycloneDX format)..."
trivy fs --format cyclonedx --output ../trivy-results/python-sbom.json .

echo "Generating SBOM (SPDX format)..."
trivy fs --format spdx-json --output ../trivy-results/python-sbom-spdx.json .

# SCA Scanning
echo "Running SCA scan..."
trivy fs --format json --output ../trivy-results/python-sca.json .

echo "Running high/critical vulnerability scan..."
trivy fs --severity HIGH,CRITICAL --format table --output ../trivy-results/python-critical.txt .

echo ""
echo "☕ Testing Java Application..."
echo "-----------------------------"
cd ../vulnerable-java-app

# SBOM Generation
echo "Generating SBOM (CycloneDX format)..."
trivy fs --format cyclonedx --output ../trivy-results/java-sbom.json .

echo "Generating SBOM (SPDX format)..."
trivy fs --format spdx-json --output ../trivy-results/java-sbom-spdx.json .

# SCA Scanning  
echo "Running SCA scan..."
trivy fs --format json --output ../trivy-results/java-sca.json .

echo "Running high/critical vulnerability scan..."
trivy fs --severity HIGH,CRITICAL --format table --output ../trivy-results/java-critical.txt .

echo ""
echo "🐹 Testing Go Application..."
echo "---------------------------"
cd ../vulnerable-go-app

# SBOM Generation
echo "Generating SBOM (CycloneDX format)..."
trivy fs --format cyclonedx --output ../trivy-results/go-sbom.json .

echo "Generating SBOM (SPDX format)..."
trivy fs --format spdx-json --output ../trivy-results/go-sbom-spdx.json .

# SCA Scanning
echo "Running SCA scan..."  
trivy fs --format json --output ../trivy-results/go-sca.json .

echo "Running high/critical vulnerability scan..."
trivy fs --severity HIGH,CRITICAL --format table --output ../trivy-results/go-critical.txt .

echo ""
echo "🐳 Testing Docker Application..."
echo "------------------------------"
cd ../vulnerable-docker-app

# Build Docker image first
echo "Building vulnerable Docker image..."
docker build -t vulnerable-test-app . > ../trivy-results/docker-build.log 2>&1

if [ $? -eq 0 ]; then
    # SBOM Generation
    echo "Generating Docker SBOM (CycloneDX format)..."
    trivy image --format cyclonedx --output ../trivy-results/docker-sbom.json vulnerable-test-app

    echo "Generating Docker SBOM (SPDX format)..."
    trivy image --format spdx-json --output ../trivy-results/docker-sbom-spdx.json vulnerable-test-app

    # SCA Scanning
    echo "Running Docker SCA scan..."
    trivy image --format json --output ../trivy-results/docker-sca.json vulnerable-test-app

    echo "Running Docker high/critical vulnerability scan..."
    trivy image --severity HIGH,CRITICAL --format table --output ../trivy-results/docker-critical.txt vulnerable-test-app
else
    echo "⚠️  Docker build failed, skipping Docker image scans"
    echo "Check docker-build.log for details"
fi

echo ""
echo "📊 Generating Summary Reports..."
echo "------------------------------"
cd ../trivy-results

# Create summary script
cat > generate_summary.py << 'EOF'
#!/usr/bin/env python3
import json
import os
import glob

def count_vulnerabilities(json_file):
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
        
        total_vulns = 0
        critical = 0
        high = 0
        medium = 0
        low = 0
        
        if 'Results' in data:
            for result in data['Results']:
                if 'Vulnerabilities' in result:
                    vulns = result['Vulnerabilities']
                    total_vulns += len(vulns)
                    for vuln in vulns:
                        severity = vuln.get('Severity', '').upper()
                        if severity == 'CRITICAL':
                            critical += 1
                        elif severity == 'HIGH':
                            high += 1
                        elif severity == 'MEDIUM':
                            medium += 1
                        elif severity == 'LOW':
                            low += 1
        
        return total_vulns, critical, high, medium, low
    except Exception as e:
        print(f"Error processing {json_file}: {e}")
        return 0, 0, 0, 0, 0

print("🔍 Trivy Vulnerability Summary Report")
print("=" * 50)
print()

apps = ['node', 'python', 'java', 'go', 'docker']
total_all = 0
critical_all = 0
high_all = 0

for app in apps:
    sca_file = f"{app}-sca.json"
    if os.path.exists(sca_file):
        total, critical, high, medium, low = count_vulnerabilities(sca_file)
        total_all += total
        critical_all += critical
        high_all += high
        
        print(f"📦 {app.upper()} Application:")
        print(f"   Total Vulnerabilities: {total}")
        print(f"   Critical: {critical}")
        print(f"   High: {high}")
        print(f"   Medium: {medium}")
        print(f"   Low: {low}")
        print()

print(f"🎯 OVERALL SUMMARY:")
print(f"   Total Vulnerabilities Found: {total_all}")
print(f"   Critical Vulnerabilities: {critical_all}")
print(f"   High Vulnerabilities: {high_all}")
print()

print("📋 Files Generated:")
for file in sorted(glob.glob("*")):
    if file.endswith(('.json', '.txt')):
        size = os.path.getsize(file)
        print(f"   {file} ({size:,} bytes)")

print()
print("✅ Testing complete! Check the trivy-results/ directory for all reports.")
print("🔗 SBOM files can be imported into other tools for further analysis.")
print("⚠️  Remember: These are intentionally vulnerable applications!")
EOF

python3 generate_summary.py > summary-report.txt
cat summary-report.txt

echo ""
echo "✅ All Trivy tests completed!"
echo "📁 Results available in: trivy-results/"
echo "📄 Summary report: trivy-results/summary-report.txt"
echo ""
echo "Generated files:"
ls -la trivy-results/ | grep -E "\\.(json|txt)$"
'''

with open("run-trivy-tests.sh", "w") as f:
    f.write(trivy_test_script)

# Make the script executable
import stat
st = os.stat("run-trivy-tests.sh")
os.chmod("run-trivy-tests.sh", st.st_mode | stat.S_IEXEC)

print("Created executable Trivy testing script: run-trivy-tests.sh")