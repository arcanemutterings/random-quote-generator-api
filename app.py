from flask import Flask, jsonify
from flask_cors import CORS
from dbhandler import *

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get_quote():
    data=getQuote()
    print(data)
    return jsonify(id=data[0][0],
                   quote=data[0][1],
                  author=data[0][2])

if __name__ == "__main__":
    app.run()