from flask import Flask, jsonify, request
from random import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if (request.method == "POST"):
        some_json = request.get_json()
        return jsonify({"'you sent'": some_json}), 200
    else:
        return jsonify({"Numero": randint(1, 100)})


@app.route('/multi/<int:num>', methods=['GET'])
def get_multiply10(num):
    return jsonify({'result': num*10})


if __name__ == '__main__':
    app.run(debug=True)
