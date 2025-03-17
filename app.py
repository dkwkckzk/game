from flask import Flask, request, jsonify
import random

app = Flask(__name__)

choices = ["rock", "paper", "scissors"]

def determine_winner(player_choice, server_choice):
    if player_choice == server_choice:
        return "draw"
    elif (player_choice == "rock" and server_choice == "scissors") or \
         (player_choice == "scissors" and server_choice == "paper") or \
         (player_choice == "paper" and server_choice == "rock"):
        return "player wins"
    else:
        return "server wins"

@app.route('/play', methods=['POST'])
def play():
    data = request.json
    player_choice = data.get("choice")
    if player_choice not in choices:
        return jsonify({"error": "Invalid choice"}), 400

    server_choice = random.choice(choices)
    result = determine_winner(player_choice, server_choice)

    return jsonify({
        "player_choice": player_choice,
        "server_choice": server_choice,
        "result": result
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
