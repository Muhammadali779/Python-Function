from rich.console import Console

console = Console()

def calculate_bmi(weight, height):
    bmi = weight / pow(height, 2)
    return bmi

def bmi_status(bmi):
    if bmi < 18.5:
        return f"BMI: {bmi:.2f} Vazn yetarli emas (Underweight)", "yellow"
    elif 18.5 <= bmi < 25:
        return f"BMI: {bmi:.2f} Normal vazn", "green"
    elif 25 <= bmi < 30:
        return f"BMI: {bmi:.2f} Ortiqcha vazn (Overweight)", "magenta"
    elif bmi >= 30:
        return f"BMI: {bmi:.2f} Semizlik (Obesity)", "red"

def main():
    while True:

        weight = float(console.input("[bold cyan]Vazn kiriting (kg): [/bold cyan]"))
        height = float(console.input("[bold cyan]Bo`yingizni kiriting (metr): [/bold cyan]"))

        bmi = calculate_bmi(weight, height)
        status_text, status_color = bmi_status(bmi)

        console.print(status_text, style=status_color)

        if weight > 0 and height > 0:
            console.print("Amaliyot muvofaqqiyatli yakunlandi!", style="bold green")
        else:
            console.print("Vazn yoki bo`y kiritilmagan yoki hato kiritilgan!", style="bold red")

        console.print("\nBMI tekshiruvi tugatilsinmi?", style="yellow")
        console.print("1. Ha", style="cyan")
        console.print("2. Yo`q", style="cyan")

        choice = console.input("[bold yellow]> [/bold yellow]")

        if choice == "1":
            console.print("BMI hisoblash dasturi tugatildi!", style="bold red")
            break
        elif choice == "2":
            continue
        else:
            console.print("Faqat (1) yoki (2) ni tanlang!", style="bold red")

main()
