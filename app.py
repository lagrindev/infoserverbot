from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "OK"

@app.route('/send', methods=['POST'])
def send():
    data = request.json
    return {"got": data}