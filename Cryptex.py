#Cryptex py file
from pyscript import web, when, display

@when("click", "#guess-button")
def AnswerCk(event):
    input_text = web.page["guess"]
    guessRAW = input_text.value
    guess = guessRAW.lower()
    if Valid(guess):
        if guess == "guess":
            display("Correct!", target= "output")
        else:
            display("Nope, Try Again", target= "output")
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
