from rich.console import Console

console = Console()

def ask_question(question, correct_answer):
    entered = input(question)

    if check_answer(entered, correct_answer):
        console.print("To`g`ri topdingiz! ", style="bold green")

    else:
        console.print("Noto`g`ri javob !", style="bold red")

def check_answer(user_answer, correct_answer):
    result = user_answer.lower() == correct_answer.lower()
    
    return result

def quiz():
    ask_question("O`zbekiston poytaxti qayer ? ", "Toshkent")

quiz()
