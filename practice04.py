from rich.console import Console

console = Console()

def get_grade(score):
  

    if 90 <= score <= 100:
        console.print("Natija A`lo: A", style="bold green")

        return f"Balingiz: {score}"
    
    elif 80 <= score < 90:
        console.print("Natija Yaxshi: B", style="bold cyan")

        return f"Balingiz: {score}"
    
    elif 70 <= score < 80:
        console.print("Natija Qoniqarli: C", style="bold yellow")
        
        return f"Balingiz: {score}"
    
    elif 60 <= score < 70:
        console.print("Natija Qoniqarsiz: F", style="bold red")
        
        return f"Balingiz: {score}"
    
    elif 0 <= score < 60:
        console.print("Natija Yomon! ", style="bold red")
        
        return f"Balingiz: {score}"
        
    
    else:
        text = console.print(f"Ball faqat (0-100) oralig`ida bo`lishi kerak", style="italic black")

        return f"Siz xato kiritgan ball: {score}"
        

score = int (input("Ball  kiriting: "))
grade = get_grade(score)

print(grade)