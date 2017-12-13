from flask import Flask, jsonify
from flask_cors import CORS
from dbhandler import *

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get_quote():
    return jsonify(getQuote())

if __name__ == "__main__":
    app.run()