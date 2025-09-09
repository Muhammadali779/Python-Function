#BMI= vazn(kg) / bo`y(m) **2

# BMI STATUSLARINI COMMENTGA YOZIB QUYDIM KERAKLI BO`LADI!

#< 18.5 → Vazn yetarli emas (Underweight)
#18.5 – 24.9 → Normal vazn
#25 – 29.9 → Ortiqcha vazn (Overweight)
#30 va undan yuqori → Semizlik (Obesity)


def calculate_bmi(weight, height):
    bmi =  weight / pow(height, 2)
    return bmi

def bmi_status(bmi):
    if bmi < 18.5:
        return f"BMI: {bmi:.2f} Vazn yetarli emas (Underweight)"
    
    elif 18.5 <= bmi < 25 :
        return f"BMI: {bmi:.2f} Normal vazn"
    
    elif 25 <= bmi < 30 :
        return f"BMI: {bmi:.2f} Ortiqcha vazn (Overweight)"
    
    elif  bmi >= 30 :
        return f"BMI: {bmi:.2f} Semizlik (Obesity)"

def main():

    while True:
        
        weight = float(input("Vazn kiriting(kg): "))      
        height = float(input("Bo`yingizni kiriting(metr): "))
        
        bmi = calculate_bmi(weight, height)
        status = bmi_status(bmi)

        print(status)

        if weight != "" and not weight < 0 and height != "" and not height < 0:
            print("Amaliyot muvofaqqiyatli yakunlandi! ")
            
        else:
            print("Vazn yoki bo`y kiritilmagan yoki hato kiritilgan!")
        
        print("BMI tekshiruvi tugatilsinmi? ")
        print("1. ha")
        print("2. yo`q")

        choise = input("> ")

        if choise == "1":
            print("BMI hisoblash dasturi tugatildi!")
            break
        elif choise == "2":
            continue
        else:
            print("Faqat (1) yoki (2) ni tanlang")

main()