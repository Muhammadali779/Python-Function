def calculate_tax(salary):
    if salary >= 5_000_000.00:
        salary += salary * 0.2
    
    else:
        salary += salary * 0.13

    return salary

def main():
    while True:

        salary = float(input("Maoshingizni kiriting: "))
        salary = calculate_tax(salary)

        if salary >= 5_000_000.00:
            print(f"20% soliq stavkasi bilan umumiy maoshingiz: {salary}")

        elif salary < 5_000_000:
            print(f"13% soliq stavkasi bilan umumiy maoshingiz: {salary}")
        
        else:
            print("Maosh manfiy bo`lmaydi! ")

        print("Dasturni tugatamizmi? ")
        print("1. Ha")
        print("2. Yo`q")

        choise = input("> ")

        if choise == "1":
            print("Dastur tugatildi! ")
            break
        elif choise == "2":
            continue
        else:
            print("Faqat 1 yoki 2 ni tanlashingiz mumkin! ")


main()

