import os
from flask import Flask, render_template, url_for
import subprocess
import json


app = Flask(__name__)

IMG_FOLDER = os.path.join('static', 'IMG')

app.config['UPLOAD_FOLDER'] = IMG_FOLDER

@app.route('/')
def index():
    img_path = url_for('static', filename='IMG/')
    IMG_LIST = os.listdir('static/IMG')
    IMG_LIST = [img_path + i for i in IMG_LIST]
    return render_template("index.html", imagelist=IMG_LIST, user_image=url_for('static', filename='IMG/logoetsit.png'))

@app.route('/ECDH')
def execute_ecdh():
    result = subprocess.run(['python', 'ECDH.py'], capture_output=True, text=True)
    output = result.stdout.strip()
    return output

@app.route('/ECIES')
def execute_ecies():
    result = subprocess.run(['python', 'ECIES.py'], capture_output=True, text=True)
    output = result.stdout.strip()
    return output

@app.route('/ECDSA')
def execute_ecdsa():
    result = subprocess.run(['python', 'ECDSA.py'], capture_output=True, text=True)
    output = result.stdout.strip()
    return output

if __name__ == '__main__':
    app.run()
