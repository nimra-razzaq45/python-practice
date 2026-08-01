#QUESTION 7- EVEN/ODD + POSITIVE/NEGATIVE
number_from_user = int(input("enter the number: "))
print("the number you entered is:",number_from_user)
if(number_from_user>0):
    print("the number is positive")
    if(number_from_user%2==0):
        print("the number is positive and even")
    else:
        print("the number is positive and odd")        
elif(number_from_user<0):
    print("the number is negative")
    if(number_from_user%2==0):
        print("the number is negative and even")
    else:
        print("the number is negative and odd")
else:
    print("the number is zero") 