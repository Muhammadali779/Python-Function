from rich.console import Console

console = Console()

secret = 23


def check_guess(secret, guess):
    
    result = guess == secret

    return result
    
def print_result(is_correct):

    if result:
        console.print(f"Siz Secret sonni topdingiz! U son {secret} edi", style="green")
    
    else:
        console.print("Siz Yashirin sonni topa olmadingiz! ", style="red")

guess = int(input("Taxminingiz: "))
result = check_guess(secret, guess)
print_result(result)