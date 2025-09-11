from rich.console import Console

console = Console()

# F = 9/5 * C +32 selsiydan farangetga utish formulasi
# C = 5/9 * (F-32) Farangeytdan selsiyga utish

def show_menu():
    console.print("""
|-------------MENU-------------|
| 1 - Selsiydan Farangetga     |
| 2 - Farangetdan Selsiyga     |
| 3 - Dasturni yakunlash       |
|______________________________|
          
""", style="cyan")

def c_to_f(celsius):

    
    F = 9 / 5 * celsius +32
    return F


def f_to_c(fahrenheit):
    
    C = 5 / 9 * (fahrenheit - 32)
    return C

def main():
    

    while True:
        show_menu()

        check = input("> ")
        if check == "1":
            celsius = float(input("Selsiyning qiymatini kiriting: "))
            farangeyt = c_to_f(celsius)
            console.print (f"{celsius}==> {farangeyt} (Farangeyt)ga teng ", style="yellow")

        elif check == "2":
            fahrenheit = float(input("Farangeytning qiymatini kiriting: "))
            celsius = f_to_c(fahrenheit)
            console.print (f"{fahrenheit}==> {celsius} (Selsiy)ga teng ", style="yellow")

        elif check == "3":
            console.print("Dastur tugadi! ", style="bold blue")
            break
        
        else:
            console.print("Bunday menu mavjud emas!", style="red")
            
main()


