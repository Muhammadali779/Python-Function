from datetime import date

def calculate_age(birth_year):

    current_year = date.today().year

    age = current_year - birth_year
    return age

name = input("Ismingiz: ")
birth_year = int(input("Tug`ulgan yilingiz: "))

age = calculate_age(birth_year)

current_year = date.today().year

if birth_year <= current_year:
    if age >= 18:
        print(f"{name}, Siz balog`atga yetgansiz! Yoshingiz {age} da")

    elif 0 <= age < 18:
        print(f"{name}, Siz balog`atga Yetmagansiz! Yoshingiz {age} da")

else:
    print("Yilingiz hozirgi yildan kichik bo`lishi kerak!")