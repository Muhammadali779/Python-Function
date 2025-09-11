from rich.console import Console

console = Console()

number = int(input("Son kiriting: "))

def is_even(number):
    result = number % 2 == 0

    return result

result = is_even(number)

def print_even_message(result):

    if result:
        console.print(f"Kiritilgan {number} son (JUFT) son", style="bold magenta")

    else:
        console.print(f"Kiritilgan {number} son (TOQ) son", style="bold red")

print_even_message(result)