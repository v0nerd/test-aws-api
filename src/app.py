from flask import Flask
from utils.run_doc import get_value 

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World from Flask and AppRunner!"

@app.route('/test')
def test():
    return get_value("test")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)