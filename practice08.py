# F = 9/5 * C +32 selsiydan farangetga utish formulasi
# C = 5/9 * (F-32) Farangeytdan selsiyga utish

def show_menu():
    print("""
|-------------MENU-------------|
| 1 - Selsiydan Farangetga     |
| 2 - Farangetdan Selsiyga     |
| 3 - Dasturni yakunlash       |
|______________________________|
          
""")

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
            print (f"{celsius}==> {farangeyt} (Farangeyt)ga teng ")

        elif check == "2":
            fahrenheit = float(input("Farangeytning qiymatini kiriting: "))
            celsius = f_to_c(fahrenheit)
            print (f"{fahrenheit}==> {celsius} (Selsiy)ga teng ")

        elif check == "3":
            print("Dastur tugadi! ")
            break
        
        else:
            print("Bunday menu mavjud emas!")
            
main()


