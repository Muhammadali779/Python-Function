phone = input("Telefon raqamingiz: ")

def is_valid_phone_number(phone):
    _phone = len(phone)

    return _phone

check = is_valid_phone_number(phone)

if len(phone) == 9 and phone.isdigit():
    print(f"Telefon raqam to`g`ri kiritldi: {phone}")

else:
    print("Hatolik bor qayta tekshiring! ")