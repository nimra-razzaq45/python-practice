#QUESTION 6- UNIVERSITY ADMISSION 
percentage_user = float(input("enter your previous percentage: "))
if(percentage_user>=60.0):
    print("congratulations, you are eligible")
    semester = input("kindly enter your semester (1st 2nd 3rd 4th): ")
    semester= semester.lower()
    if(semester=="1st"):
        print("eligible for admission")
    elif(semester=="2nd"):
        print("eligible for admission")    
    elif(semester=="3rd"):
        print("eligible for admission")    
    elif(semester=="4th"):
        print("eligible for internship")    
    else:
        print("invalid input")
else:
    print("not eligible")