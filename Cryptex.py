#Cryptex py file
from pyscript import web, when, display

@when("click", "#guess-button")
def AnswerCk(event):
    input_text = web.page["guess"]
    guess = input_text.value
    if guess == "guess":
        display("Correct!", target= "output")
    else:
        display("Nope, Try Again", target= "output")
