# test case uchun suzlar: 
# non, level, otto, radar, aka,  ikki, alla

def is_palindrome(text):
    _text = text[::-1]
    is_true = text == _text

    return is_true

def main():

    text = input("Matn kiriting: ")
    is_palindrome(text)
    is_true = is_palindrome(text)

    if is_true:
        print(is_true)
        print("Ha, Haqiqatdan ham matnning teskari uqilgani ham bir biriga teng!")

    else:
        print("Yo`q, Matn teskari uqilganda teng emas!")

main()
