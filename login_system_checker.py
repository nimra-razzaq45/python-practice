# #q1 login system checker
user_name = input("kindly enter your username: ")
password = input("kindly enter your password: ")
correct_username = "admin"
correct_password = "pass123"
print("the username entered is:",user_name)
print("the password entered is:",password)
if (user_name == correct_username and password == correct_password):
    print("login successfull")
elif(user_name == correct_username and not password == correct_password):
    print("wrong password")  
elif(not user_name == correct_username and password == correct_password):
    print("wrong username")      
else:
    print("invalid username and password") 