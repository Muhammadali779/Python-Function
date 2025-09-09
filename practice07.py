
questions = "O`zbekistonda nechta viloyat bor?"

correct_answer = "12"

print(questions)

print("Variantlar: \n13 ta \n11 ta \n10 ta \n12 ta")

user_answer = input("> ")

def check_answer(user_answer, correct_answer):
    
    if user_answer == "12":
        print("Tog`ri topdingiz! ")
    
    else:
        print("Noto`g`ri javob!! ")

check_answer(user_answer, correct_answer)