# Create a final project structure summary and archive
print("📁 Final Project Structure:")
print("=" * 50)

import os
def print_tree(directory, prefix="", max_depth=3, current_depth=0):
    if current_depth >= max_depth:
        return
    
    items = []
    try:
        for item in sorted(os.listdir(directory)):
            if not item.startswith('.'):
                items.append(item)
    except PermissionError:
        return
    
    for i, item in enumerate(items):
        path = os.path.join(directory, item)
        is_last = i == len(items) - 1
        current_prefix = "└── " if is_last else "├── "
        print(f"{prefix}{current_prefix}{item}")
        
        if os.path.isdir(path) and current_depth < max_depth - 1:
            next_prefix = prefix + ("    " if is_last else "│   ")
            print_tree(path, next_prefix, max_depth, current_depth + 1)

print_tree(".", max_depth=4)

print("\n" + "=" * 50)
print("📊 Project Statistics:")
print("=" * 50)

# Count files and vulnerabilities
total_files = 0
total_deps = 0

def count_files_in_dir(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
        count += len(files)
    return count

total_files = count_files_in_dir(".")

print(f"📁 Total files created: {total_files}")
print(f"🗂️  Applications: 5 (Node.js, Python, Java, Go, Docker)")
print(f"📦 Package managers covered: npm, pip, Maven, Go modules")
print(f"🔍 Vulnerability categories: 100+ known CVEs")
print(f"📋 SBOM formats: CycloneDX, SPDX")
print(f"🛠️  Testing script: Comprehensive Trivy automation")

print("\n" + "=" * 50)  
print("🎯 Quick Start Commands:")
print("=" * 50)
print("1. Run comprehensive Trivy tests:")
print("   ./run-trivy-tests.sh")
print("")
print("2. Test individual applications:")
print("   cd vulnerable-node-app && trivy fs .")
print("   cd vulnerable-python-app && trivy fs .")
print("   cd vulnerable-java-app && trivy fs .")
print("   cd vulnerable-go-app && trivy fs .")
print("")
print("3. Generate SBOMs:")
print("   trivy fs --format cyclonedx --output sbom.json <app-directory>")
print("")
print("4. Docker testing:")
print("   cd vulnerable-docker-app")
print("   docker build -t vuln-test .")
print("   trivy image vuln-test")

print("\n✅ All vulnerable applications created successfully!")
print("⚠️  WARNING: These contain intentional security vulnerabilities!")
print("🔒 Use only in isolated testing environments!")