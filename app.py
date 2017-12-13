from flask import Flask, jsonify
from dbhandler import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_quote():
    return jsonify(getQuote())

if __name__ == "__main__":
    app.run()