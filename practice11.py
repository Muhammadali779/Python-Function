from rich.console import Console

console = Console()


def calculate_tax(salary):
    if salary >= 5_000_000.00:
        tax = salary * 0.2
    
    else:
        tax = salary * 0.13

    return tax

def main():
    while True:

        salary = float(input("Maoshingizni kiriting: "))
        tax = calculate_tax(salary)

        if salary >= 5_000_000.00:
            console.print(f"20% soliq stavkasi bilan umumiy soliq: {tax}", style="bold yellow")

        elif salary < 5_000_000:
            console.print(f"13% soliq stavkasi bilan umumiy soliq: {tax}", style="bold yellow")
        
        else:
            console.print("Maosh manfiy bo`lmaydi! ", style="red")

        console.print("Dasturni tugatamizmi? ", style="cyan")
        console.print("1. Ha", style="cyan")
        console.print("2. Yo`q", style="cyan")

        choise = input("> ")

        if choise == "1":
            console.print("Dastur tugatildi! ", style="red")
            break
        elif choise == "2":
            continue
        else:
            console.print("Faqat 1 yoki 2 ni tanlashingiz mumkin! ",style="bold red")


main()

