
def get_grade(score):
  

    if 90 <= score <= 100:
        return "A"
    
    elif 80 <= score < 90:
        return "B"
    
    elif 70 <= score < 80:
        return "C"
    
    elif 60 <= score < 70:
        return "F"
    
    elif 0 <= score < 60:
        print("Natija yomon! ")
        
    
    else:
        print("Ball faqat (0-100) oralig`ida bo`lishi kerak")
        

score = int (input("Ball  kiriting: "))
grade = get_grade(score)

print(grade)