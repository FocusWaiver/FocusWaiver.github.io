#Cryptex py file
from pyscript import web, when

print("It worked?")

@when("click", "#guess-button")
def AnswerCk(event):
    input_text = web.page["english"]
    guess = input_text.value
    print(guess)