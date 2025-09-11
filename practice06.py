from rich.console import Console

console = Console()

phone = input("Telefon raqamingiz: ")

def is_valid_phone_number(phone):
    _phone = len(phone) == 9 and phone.isdigit()

    return _phone

check = is_valid_phone_number(phone)

if check:
    console.print(f"Telefon raqam to`g`ri kiritldi: {phone}", style="bold green")

else:
    console.print("Hatolik bor qayta tekshiring! ", style="bold red")