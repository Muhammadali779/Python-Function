
number = int(input("Son kiriting: "))
def is_even(number):
    result = number % 2

    return result

even_num = is_even(number)

if even_num == 0:
    print(f"Kiritilgan {number} son (JUFT) son")


else:
    print(f"Kiritilgan {number} son (TOQ) son")