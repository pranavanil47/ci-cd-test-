from flask import Flask, request, redirect, render_template_string
import sqlite3
import os
import subprocess
import json
import yaml
import pickle
import hashlib
import random
import requests

app = Flask(__name__)

# --- Hardcoded secrets ---
API_KEY = "sk_test_51LkdjflkASDFjalksdjf"
DB_PASSWORD = "p@ssword123"
JWT_SECRET = "supersecretjwtkey"

@app.route("/")
def index():
    return "Welcome to Vulnerable App!"

# --- SQL Injection ---
@app.route("/login")
def login():
    username = request.args.get("username")
    password = request.args.get("password")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    if user:
        return "Logged in"
    else:
        return "Invalid"

# --- Command Injection ---
@app.route("/ping")
def ping():
    ip = request.args.get("ip")
    output = subprocess.getoutput(f"ping -c 1 {ip}")
    return output

# --- Path Traversal ---
@app.route("/read")
def read_file():
    filename = request.args.get("file")
    with open(f"./files/{filename}", "r") as f:
        return f.read()

# --- Insecure Deserialization ---
@app.route("/deserialize", methods=["POST"])
def deserialize():
    data = request.data
    obj = pickle.loads(data)
    return str(obj)

# --- NoSQL Injection (MongoDB style) ---
@app.route("/search")
def search():
    user_input = request.args.get("user")
    query = {"username": user_input}
    # This is pseudocode, simulate NoSQL injection
    return json.dumps({"query": str(query)})

# --- XSS ---
@app.route("/greet")
def greet():
    name = request.args.get("name", "Guest")
    return render_template_string(f"<h1>Hello {name}</h1>")

# --- Unsafe YAML load ---
@app.route("/yaml", methods=["POST"])
def unsafe_yaml():
    data = request.data
    config = yaml.load(data, Loader=yaml.FullLoader)
    return str(config)

# --- Open Redirect ---
@app.route("/redirect")
def redir():
    url = request.args.get("next")
    return redirect(url)

# --- Weak Hash & Insecure Random ---
@app.route("/hash")
def weak_hash():
    password = request.args.get("pw")
    salt = str(random.random())
    return hashlib.md5((salt + password).encode()).hexdigest()

# --- Eval and Exec ---
@app.route("/exec")
def run_exec():
    code = request.args.get("code")
    result = eval(code)  # Dangerous
    return str(result)

# --- SSRF ---
@app.route("/ssrf")
def ssrf():
    url = request.args.get("url")
    res = requests.get(url)
    return res.text

if __name__ == "__main__":
    app.run(debug=True)
