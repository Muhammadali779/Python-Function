def show_menu():
    print("""
|-----------------MENU-----------------|
| 1 - deposit (Pul To`ldirish)         |
| 2 - withdraw (Pul yechish)           |
| 3 - check_balance(Pulni tekshirish)  |
| 4 - Amaliyotni yakunlash             |
|______________________________________|
          
""")
    
def deposit(balance, amount):
    if amount > 0:
        balance += amount
    return balance

def withdraw(balance, amount):
    if amount <= balance:
        balance -= amount
    else:
        print("Mablag` yetarli emas!")
    return balance

def check_balance(balance):
    print(f"Balansingiz: {balance}")

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
            print("Amaliyot yakunlandi! ")

            break

        else:
            print("Bunday menu mavjud emas! ")

main()
