from rich.console import Console

console = Console()


def show_menu():
    console.print("""
|-----------------MENU-----------------|
| 1 - deposit (Pul To`ldirish)         |
| 2 - withdraw (Pul yechish)           |
| 3 - check_balance (Pulni tekshirish) |
| 4 - Amaliyotni yakunlash             |
|______________________________________|
          
""", style="bold cyan")
    
def deposit(balance, amount):
    if amount > 0:
        balance += amount
    return balance

def withdraw(balance, amount):
    if amount <= balance:
        balance -= amount
    else:
        console.print("Mablag` yetarli emas!", style="red")
    return balance

def check_balance(balance):
    console.print(f"Balansingiz: {balance}", style="green")

def main():

    balance = 100_000.00

    while True:
        show_menu()

        check = input("> ")
        if check == "1":
            amount = float(input("Qancha pul tashlamoqchisiz: "))
            balance = deposit(balance, amount)
        
        elif check == "2":
            amount = float(input("Qancha pul Yechib olmoqchisiz: "))
            balance = withdraw(balance, amount)
        
        elif check == "3":
            check_balance(balance)

        elif check == "4":
            console.print("Amaliyot yakunlandi! ", style="bold cyan")

            break

        else:
            console.print("Bunday menu mavjud emas! ", style="bold red")

main()
