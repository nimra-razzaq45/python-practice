#q4 movie ticket pricing
user_age = int(input("enter your age: "))
student_check= input("are you a student: ")
student_check= student_check.upper()
if(student_check=="YES" or student_check=="NO"):
    print("welcome to the booking page:")
    print("pricing rules: ")
    if(user_age<5):
        print("ticket free")
    elif(user_age>=5 and user_age<=12):
        print("ticket price is RS 300") 
    elif(user_age>=60):
        print("ticket price RS 200 (senior citizen discount)")
    elif(user_age>=13 and user_age<60):
        print("normal price RS 500")
        if(student_check=="YES"):
            print("special discount for students RS 400")
        else:
            print("no discount")
else:
    print("invalid answer. only yes or no is required")