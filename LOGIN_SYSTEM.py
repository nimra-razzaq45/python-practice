#QUESTION 3- LOGIN SYSTEM
correct_username = "admin"
correct_password = "python123"
username= input("enter username: ")
username=username.lower()
if(username==correct_username):
    print("valid username")
    user_password=input("enter password: ")
    user_password=user_password.lower()
    if(user_password==correct_password):
        print("correct password")
        user_role=input("kindly enter your role: ")
        user_role=user_role.lower()
        if(user_role=="admin"):
            print("welcome admin")
        elif(user_role=="teacher"):
            print("welcome teacher")
        elif(user_role=="student"):
            print("welcome student")
        else:
            print("unknown role")            
    else:
        print("invalid password","\nplease enter the correct password to login")        
else:
    print("invalid username","\nplease enter the correct username to login") 