from rich.console import Console

console = Console()


def is_palindrome(text):
    _text = text[::-1]
    is_true = text == _text
    return is_true

def main():
    text = input("Matn kiriting: ")
    is_true = is_palindrome(text)

    if is_true:
        console.print(is_true, style="bold green")
        console.print("Haqiqatdan ham matnning teskari o‘qilgani bir xil!", style="green")
    else:
        console.print(is_true, style="bold red")
        console.print("Matn teskari o‘qilganda teng emas!", style="red")

main()
