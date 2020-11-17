from flask import Flask, render_template, jsonify, request
import random
import json

app = Flask(__name__)


lotto_numbers = list(range(1,46))

@app.route("/")
def hello():

    return render_template("index.html", variable=choice)

@app.route("/bot-choice",methods=['POST'])
def choice():
    print(request.get_data())
    params = json.loads(request.get_data())

    positions = params["cells"]
    moves = params["moves"]
    res = computer_hard(positions,moves)
    return jsonify(res)

def computer_hard(positions, moves):
    res = {"choose" : -1}


        return res


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)