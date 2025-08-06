# Create Python Flask application
flask_app_content = '''#!/usr/bin/env python3
"""
Vulnerable Flask application for Trivy SBOM and SCA testing
Contains intentionally vulnerable dependencies and code patterns
"""

import os
import yaml
import pickle
import subprocess
from flask import Flask, request, render_template_string, jsonify
from jinja2 import Template
import requests
import sqlite3
from cryptography.fernet import Fernet
import paramiko
from lxml import etree
from PIL import Image
import redis

app = Flask(__name__)
app.secret_key = "insecure_secret_key_for_testing"

# Vulnerable configurations
app.config['DEBUG'] = True  # Never use in production

# Database setup with SQLAlchemy (vulnerable version)
DATABASE = 'vulnerable_app.db'

@app.route('/')
def home():
    return jsonify({
        "message": "Vulnerable Flask app for Trivy testing",
        "vulnerabilities": [
            "Django 1.11.0 - Multiple CVEs",
            "Flask 0.12.2 - Security issues",
            "Jinja2 2.7.2 - Template injection",
            "PyYAML 3.12 - Arbitrary code execution",
            "Requests 2.19.1 - CVE-2018-18074",
            "Pillow 5.2.0 - Image processing CVEs",
            "And many more vulnerable dependencies..."
        ],
        "endpoints": [
            "/template - Template injection demo",
            "/yaml - YAML deserialization demo", 
            "/pickle - Pickle deserialization demo",
            "/xml - XXE vulnerability demo",
            "/sql - SQL injection demo"
        ]
    })

@app.route('/template')
def template_injection():
    """Vulnerable template rendering using old Jinja2"""
    user_input = request.args.get('template', 'Hello {{name}}!')
    name = request.args.get('name', 'World')
    
    # Vulnerable template rendering - allows code injection
    template = Template(user_input)
    result = template.render(name=name)
    
    return f"Rendered template: {result}"

@app.route('/yaml', methods=['POST'])
def yaml_load():
    """Vulnerable YAML deserialization using PyYAML 3.12"""
    data = request.get_data()
    
    try:
        # Vulnerable yaml.load - allows arbitrary code execution
        parsed = yaml.load(data)
        return jsonify({"parsed": str(parsed)})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/pickle', methods=['POST']) 
def pickle_load():
    """Vulnerable pickle deserialization"""
    data = request.get_data()
    
    try:
        # Vulnerable pickle deserialization - allows code execution
        result = pickle.loads(data)
        return jsonify({"result": str(result)})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/xml', methods=['POST'])
def xml_parse():
    """XXE vulnerability using lxml 4.2.1"""
    xml_data = request.get_data()
    
    try:
        # Vulnerable XML parsing - allows XXE attacks
        parser = etree.XMLParser(resolve_entities=True)
        root = etree.fromstring(xml_data, parser)
        return jsonify({"parsed": etree.tostring(root, encoding='unicode')})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/sql')
def sql_injection():
    """SQL injection vulnerability"""
    user_id = request.args.get('id', '1')
    
    # Vulnerable SQL query - allows injection
    query = f"SELECT * FROM users WHERE id = {user_id}"
    
    try:
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE users (id INTEGER, name TEXT)")
        cursor.execute("INSERT INTO users VALUES (1, 'admin'), (2, 'user')")
        cursor.execute(query)  # Vulnerable query
        results = cursor.fetchall()
        conn.close()
        
        return jsonify({"query": query, "results": results})
    except Exception as e:
        return jsonify({"error": str(e), "query": query})

@app.route('/request')
def make_request():
    """SSRF vulnerability using requests 2.19.1"""
    url = request.args.get('url', 'http://httpbin.org/get')
    
    try:
        # Vulnerable - allows SSRF attacks
        response = requests.get(url, timeout=5)
        return jsonify({
            "url": url,
            "status": response.status_code,
            "content": response.text[:1000]
        })
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    print("Starting vulnerable Flask application...")
    print("This app contains multiple vulnerable dependencies for Trivy testing")
    app.run(debug=True, host='0.0.0.0', port=5000)
'''

with open("vulnerable-python-app/app.py", "w") as f:
    f.write(flask_app_content)

print("Created app.py for Python vulnerable application")