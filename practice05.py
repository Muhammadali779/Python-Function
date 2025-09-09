secret = 23
guess = int(input("Taxminingiz: "))

def check_guess(secret, guess):
    
    if guess < secret:
        print("Secret son kattaroq! ")
    
    elif guess > secret:
        print("Secret son kichikroq! ")  

    else:
        print(f"Siz Secret sonni topdingiz! U son {secret} edi")
        

check_guess(secret, guess)