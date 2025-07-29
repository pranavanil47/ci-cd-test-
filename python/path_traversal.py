
from flask import Flask, request, send_file
app = Flask(__name__)
@app.route('/download')
def download():
    file = request.args.get('file')
    # VULNERABLE: no sanitization of file path
    return send_file('/var/www/uploads/' + file)  # CWE-22
