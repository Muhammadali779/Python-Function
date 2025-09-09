def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2
    
def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("0 ga bo`lib bo`lmaydi!")

def main():
    while True:
        num1 = int(input("1- sonni kiriting: "))
        num2 = int(input("2- sonni kiriting: "))
        amal = input("Amalni tanlang: ")

        if amal == "+":
            result = add(num1, num2)

        elif amal == "-":
            result = subtract(num1, num2)
        
        elif amal == "*":
            result = multiply(num1, num2)

        elif amal == "/":
            result = divide(num1, num2)

        else:
            print("Bunday amal mavjud emas! ")
        
        print(result)

        print("Hisoblashni davom etamizmi?")
        print("Ha yoki Yo`q")

        choise = input("> ")
        _choise = choise.lower()

        if _choise == "ha":
            continue
        
        elif _choise == "yo`q":
            break

        else:
            print("Faqat Ha yoki Yo`q kirita olasiz! ")

main()
