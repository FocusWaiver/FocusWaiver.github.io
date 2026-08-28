#Cryptex py file
from pyscript import web, when, display
correct = "guess"
@when("click", "#guess-button")
def AnswerCk(event):
    input_text = web.page["guess"]
    guessRAW = input_text.value
    guess = guessRAW.lower()
    if Valid(guess):
        if guess == correct:
            display("Correct! Great Job!", target= "output")
        else:
            score = scorer(guess)
            display("Incorrect.",guess, "scored: ",score, target= "output")
    else:
        display("Sorry, your guess must be 5 letters.")


def Valid(ans):
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


def scorer(ans):
    score_index = []
    place = 0
    score = 0
    correctlist = list(correct)
    anslist = list(ans)
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