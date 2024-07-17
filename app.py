import random
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


def determine_win(prediction, prev_roll, new_roll):
    if prediction == "equal":
        return prev_roll == new_roll
    elif prediction == "higher":
        return new_roll > prev_roll
    else:
        return new_roll < prev_roll


@app.route('/')
def index():
    initial_number = random.randint(1, 6)
    return render_template('index.html', initial_number=initial_number)


@app.route('/roll', methods=["POST"])
def dice_roll():
    body = request.json
    prev_roll = body['previous']
    prediction = body['prediction']
    new_roll = random.randint(1, 6)

    return jsonify({
        "roll": new_roll,
        "win": determine_win(prediction, prev_roll, new_roll)
    })
