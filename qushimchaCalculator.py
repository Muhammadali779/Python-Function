from math import sqrt
from rich.console import Console

console = Console()

def add(a, b):           
    return a + b

def subtract(a, b):               
    return a - b

def multiply(a, b): 
    return a * b

def divide(a, b):
    if b == 0:
        console.print("Nolga bo‘lish mumkin emas!", style="bold red")
        return None
    return a / b

def kv(a, b): 
    return a ** b

def _sqrt(a): 
    return sqrt(a)

def percentage(a, b): 
    return (a * b) / 100     


def main():

    while True:

        console.print("""
|-------------MENU-------------|
| 1 - Qo‘shish                 |
| 2 - Ayirish                  |
| 3 - Ko‘paytirish             |
| 4 - Bo‘lish                  |
| 5 - Daraja                   |
| 6 - Kvadrat ildizni topish   |
| 7 - Foizini topish           |
| 8- Dasturni yakunlash        |
|______________________________|
        
""", style="bold cyan")
        
        choice = input("> ")

        if choice in ["1", "2", "3", "4", "5", "7"]:
            a = float(input("1-sonni kiriting: "))
            b = float(input("2-sonni kiriting: "))

        if choice == "1":
            result = add(a, b)
            console.print(f"Natija: {result}", style="bold green")

        elif choice == "2":
            result = subtract(a, b)
            console.print(f"Natija: {result}", style="bold green")

        elif choice == "3":
            result = multiply(a, b)
            console.print(f"Natija: {result}", style="bold green")

        elif choice == "4":
            result = divide(a, b)
            if result is not None:
                console.print(f"Natija: {result}", style="bold green")

        elif choice == "5":
            result = kv(a, b)
            console.print(f"Natija: {result}", style="bold green")

        elif choice == "6":
            a = float(input("Sonni kiriting: "))
            result = _sqrt(a)
            console.print(f"Natija: {result}", style="bold green")
            
        elif choice == "7":
            result = percentage(a, b)
            console.print(f"Natija: {result}", style="bold green")
        
        elif choice == "8":
            console.print("Dastur tugatildi!", style="bold red")
            break

        else:
            console.print("Bunday bo`lim mavjud emas!", style="bold yellow")


main()
