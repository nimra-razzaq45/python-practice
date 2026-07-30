# #q1 login system checker
# user_name = input("kindly enter your username: ")
# password = input("kindly enter your password: ")
# correct_username = "admin"
# correct_password = "pass123"
# print("the username entered is:",user_name)
# print("the password entered is:",password)
# if (user_name == correct_username and password == correct_password):
#     print("login successfull")
# elif(user_name == correct_username and not password == correct_password):
#     print("wrong password")  
# elif(not user_name == correct_username and password == correct_password):
#     print("wrong username")      
# else:
#     print("invalid username and password")    

# #q2 grade calculator with validation
# marks=int(input("enter marks between 0-100: "))
# is_fail = True
# if (marks<0 or marks>100) :
#     print("invalid marks")
# elif (marks>0 or marks<100):
#     print("valid marks")
#     if(marks>=90):
#         print("A+",not is_fail)
#     elif(marks>=80 and marks<=89):
#         print("A",not is_fail)
#     elif(marks>=70 and marks<=79):
#         print("B",not is_fail)
#     elif(marks>=60 and marks<=69):
#         print("C",not is_fail)
#     else:
#         print("Fail", is_fail)    
# else:
#     print("invalid")

#q3 atm withdrawal system
# user_account = float(input("enter your account balance: "))
# withdraw_amount = float(input("how much you want to withdraw: "))
# if(withdraw_amount>user_account):
#     print("insufficient balance")     
# elif(withdraw_amount<=0):
#     print("invalid amount")  
# elif(withdraw_amount<=user_account and withdraw_amount>100):
#     print("withdrawal successful","\nyour new balance is",user_account-withdraw_amount)
# elif(withdraw_amount<=user_account and withdraw_amount<100):
#     print("minimum withdrawal amount is 100") 
# print("thankyou for your patience")             

#q4 movie ticket pricing
# user_age = int(input("enter your age: "))
# student_check= input("are you a student: ")
# student_check= student_check.upper()
# if(student_check=="YES" or student_check=="NO"):
#     print("welcome to the booking page:")
#     print("pricing rules: ")
#     if(user_age<5):
#         print("ticket free")
#     elif(user_age>=5 and user_age<=12):
#         print("ticket price is RS 300") 
#     elif(user_age>=60):
#         print("ticket price RS 200 (senior citizen discount)")
#     elif(user_age>=13 and user_age<60):
#         print("normal price RS 500")
#         if(student_check=="YES"):
#             print("special discount for students RS 400")
#         else:
#             print("no discount")
# else:
#     print("invalid answer. only yes or no is required")    

#q5 traffic light simulator
# user_color = input("enter a color e.g red yellow green: ")
# print("the color you entered: ",user_color)
# user_color=user_color.upper()
# if(user_color=="RED"):
#     print("STOP")
# elif(user_color=="YELLOW"):
#     print("GET READY")
# elif(user_color=="GREEN"):
#     print("GO")
# else:
#     print("invalid color. only red green yellow are allowed :)")

#q6 ride fare calculator (uber/careem type)
distance = float(input("enter the distance: "))
time = input("enter the time (day/night): ")
time=time.upper()
rain = input("is there rain? (yes/no) ")
rain=rain.upper()
print("fare rules: ")
base_fare = 50 + (distance * 20)
if(time=="NIGHT"):
    print("fare with 20% extra: ",base_fare * 20)
elif(rain=="YES"):
    print("we will charge extra.")
    if(time=="DAY" or time=="NIGHT"):
        print("we charge extra 100 RS",base_fare+100)
        