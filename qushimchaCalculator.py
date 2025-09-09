from math import sqrt

def add(a, b):           
    return a + b

def subtract(a, b):               
    return a - b

def multiply(a, b): 
    return a * b

def divide(a, b):
    if b == 0:

        print("Nolga bo‘lish mumkin emas!")    
    return a / b

def kv(a, b): 
    return a ** b

def _sqrt(a): 
    return sqrt(a)

def percentage(a, b): 
    return (a * b) / 100     # a sonning b % ni hisoblash uchun


def main():

    while True:

        print("""
|-------------MENU-------------|
| 1 - Qo‘shish                 |
| 2 - Ayirish                  |
| 3 - Ko‘paytirish             |
| 4 - Bo‘lish                  |
| 5 - Daraja                   |
| 6 - Kvadrat ildizni topish   |
| 7 - Foizini topish           |
| 8 - Dasturni yakunlash       |
|______________________________|
          
""")
        choice = input("> ")

          # bu yerda sal boshqacharoq logica qildim agar tanlov faqat hisoblash amallari ichida bulsa
          # a va b sonlar so`raladi so`ngra ular ustida amallar bajariladi
        if choice in ["1", "2", "3", "4", "5", "7"]:
            a = float(input("1-sonni kiriting: "))
            b = float(input("2-sonni kiriting: "))

        if choice == "1":
            result = add(a, b)
            print(f"Natija: {result}")

        elif choice == "2":
            result = subtract(a, b)
            print(f"Natija: {result}")

        elif choice == "3":
            result = multiply(a, b)
            print(f"Natija: {result}")

        elif choice == "4":
            result = divide(a, b)
            print(f"Natija: {result}")

        elif choice == "5":
            result = kv(a, b)
            print(f"Natija: {result}")

        elif choice == "6":
            result = _sqrt(a)
            print(f"Natija: {result}")
            
        elif choice == "7":
            result = percentage(a, b)
            print(f"Natija: {result}")
        
        elif choice == "8":
            print("Dastur tugatildi!")
            break

        else:
            print("Bunday bo`lim mavjud emas! ")


main()
