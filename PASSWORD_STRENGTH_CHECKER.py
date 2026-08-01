#QUESTION 9- PASSWORD STRENGTH CHECKER
password_user= input("enter the password: ")
if(len(password_user)<8):
    print("the password you entered is weak")
elif(len(password_user)>=8):
    print("now you have entered the correct password")
    if(password_user==password_user.isdigit()):
        print("medium password")    
    elif(password_user==password_user.isalnum()):
        print("strong password")
    else:
        print("not right") 
else:
    print("invalid password")