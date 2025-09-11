from rich.console import Console

console = Console()

def is_strong_password(password):
    
    checked = len(password) >= 8
    if checked:
        return checked
    
def main():

    
    while True:

        password = input("Parol yarating: ")
        checked = is_strong_password(password)

        if checked:
            console.print("Siz KUCHLI parol yaratdingiz! ", style="bold blue")

            break

        else:
            console.print("Parolingiz KUCHSIZ qayta urinib ko`ring! ", style="bold red")


main()