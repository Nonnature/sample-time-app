from flask import Flask, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def get_time():
    return jsonify({"now": datetime.now(timezone.utc).isoformat()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
