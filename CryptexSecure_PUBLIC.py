#CryptexSecure, Updated with the help of Claude
#Cryptex.py is original file
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# No hits from other websites
CORS(app, origins=["https://focuswaiver.github.io"])

correct = "world"

def score_guess(input):
    score_index = []
    place = 0
    score = 0
    correctlist = list(correct)
    anslist = list(input)
    #letters in the right place?
    for i in range(5):
        if anslist[i] == correctlist[i]:
            score_index.append(1)
            score +=2
        else:
            score_index.append(0)
    #Removing correctly placed letters from contention
    for a in score_index:
        if a > 0:
            anslist[place] = "*"
            correctlist[place] = 0
        place += 1
    #Adding one point for letters in the word that are not in position
    for b in anslist:
        for c in correctlist:
            if b == c:
                score += 1
    return score

def valid(ans):
    anslist = list(ans)
    Vkey = "abcdefghijklmnopqrstuvwxyz"
    if len(ans) != 5:
        return False
    else:
        #check against valid characters
        for i in anslist:
            if Vkey.find(i) < 0:
                return False
        return True

@app.route("/process_guess", methods=['POST'])
def process_guess():
    guess = request.json.get("guess","").lower()
    #check validity
    if valid(guess):
        if guess == correct:
            result = {"score": 10, "winner": True}
        else:
            score = score_guess(guess)
            result = {"score": score, "winner": False}
    else:
        result = {"score": "Must be 5 letters", "winner":False}
    return jsonify(result)

if __name__ == "__main__":
    app.run()
