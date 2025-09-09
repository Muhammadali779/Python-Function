def is_strong_password(password):
    
    checked = len(password) >= 8 and password.isalnum()
    if checked:
        return checked
    
def main():

    
    while True:

        password = input("Parol yarating: ")
        checked = is_strong_password(password)
        if checked:
            print("Siz KUCHLI parol yaratdingiz! ")
            break
        else:
            print("Parolingiz KUCHSIZ qayta urinib ko`ring! ")


main()