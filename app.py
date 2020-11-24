from flask import Flask, render_template, jsonify, request
import random
import json

app = Flask(__name__)

x = 1
o = 3

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

    if moves == 0:
        res["choose"] = 4
        return res

    if moves == 2:
        if (positions[0] == o) or (positions[1] == o):
            res["choose"] = 2
        elif (positions[2] == o) or (positions[5] == o):
            res["choose"] = 8
        elif (positions[7] == o) or (positions[8] == o):
            res["choose"] = 6
        else:
            res["choose"] = 0
        return res

    if moves == 4:
        if positions[2] == x:
            if positions[6] == o:
                if positions[0] == o:
                    res["choose"] = 3
                else:
                    res["choose"] = 5
            else:
                res["choose"] = 6 # 승

        elif positions[8] == x:
            if positions[0] == o:
                if positions[2] == o:
                    res["choose"] = 1
                else:
                    res["choose"] = 7
            else:
                res["choose"] = 0
        elif positions[6] == x:
            if positions[2] == o:
                if positions[8] == o:
                    res["choose"] = 5
                else:
                    res["choose"] = 3
            else:
                res["choose"] = 2
        # positions[0] == x
        else:
            if positions[8] == o:
                if positions[6] == o:
                    res["choose"] = 7
                else:
                    res["choose"] = 1
            else:
                res["choose"] = 8
        return res

    if moves == 6:
        if positions[2] == x:
            if positions[5] == x:
                if positions[3] == o:
                    res["choose"] = 8 # 승
                else:
                    res["choose"] = 3 # 승
            else: # positions[3] == x
                if positions[5] == o: # 막는 경우
                    res["choose"] = 7
                else: # 안 막는 경우
                    res["choose"] = 5 # 승

        elif positions[8] == x:
            if positions[7] == x:
                if positions[1] == o:
                    res["choose"] = 6 # 승
                else:
                    res["choose"] = 1 # 승
            else: # positions[3] == x
                if positions[7] == o: # 막는 경우
                    res["choose"] = 3
                else: # 안 막는 경우
                    res["choose"] = 7 # 승
        elif positions[6] == x:
            if positions[3] == x:
                if positions[5] == o:
                    res["choose"] = 0 # 승
                else:
                    res["choose"] = 5 # 승
            else: # positions[3] == x
                if positions[3] == o: # 막는 경우
                    res["choose"] = 1
                else: # 안 막는 경우
                    res["choose"] = 3 # 승
        else:
            if positions[1] == x:
                if positions[7] == o:
                    res["choose"] = 2 # 승
                else:
                    res["choose"] = 7 # 승
            else: # positions[3] == x
                if positions[1] == o: # 막는 경우
                    res["choose"] = 5
                else: # 안 막는 경우
                    res["choose"] = 1 # 승

        return res

    if moves == 8:
        if positions[2] == x:
            if positions[1] == o:
                res["choose"] = 8 # 무승부
            else:
                res["choose"] = 1
        elif positions[8] == x:
            if positions[5] == o:
                res["choose"] = 6 # 무승부
            else:
                res["choose"] = 5
        elif positions[6] == x:
            if positions[7] == o:
                res["choose"] = 0 # 무승부
            else:
                res["choose"] = 7
        else:
            if positions[3] == o:
                res["choose"] = 2 # 무승부
            else:
                res["choose"] = 3
        #x = 1
        #o = 3

        #0 1 2
        #3 4 5
        #6 7 8
        return res




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)