#q1
# age = int(input("enter age: "))
# if(age>=18):
#     print("eligible for CNIC")
# else:
#     print("not eligible")

# #q2
# number = int(input("\nenter number: "))
# if(number<0):
#     print("negative number")
# else:
#     print("positive")

#q3 
# password= input("enter password: ")
# correct_password = "Python123" 
# if(password==correct_password):
#     print("access granted")
# else:
#     print("access denied")

# #q4
# marks= int(input("\nenter marks: "))
# if(marks>=50):
#     print("pass")
# else:
#     ("fail") 

# #q5
# num1=int(input("\nenter first number: ")) 
# num2=int(input("enter second number: ")) 
# if(num1>num2):
#     print ("first number is greater")
# else:
#     print("second number is greater or equal")     

#DETAILED PRACTICE:
#QUESTION 1- STUDENT GRADE SYSTEM
# marks = int(input("enter your marks: "))
# if(marks>=0 and marks<=100):
#     print("valid marks") 
#     if(marks>=90):
#         print("A+")
#     elif(marks>=80):
#         print("A")
#     elif(marks>=70):
#         print("B")
#     elif(marks>=60):
#         print("C")
#     elif(marks>=50):
#         print("D")
#     else:
#         print("fail")    
# else:
#     print("invalid marks")    

# #QUESTION 2- ATM WITHDRAWAL 
# account_balance= int(50000)
# withdrawal_amount= int(input("enter the amount to withdraw: "))
# if(withdrawal_amount<=account_balance):
#     print("the amount you want to withdraw is:",withdrawal_amount)
#     user_pin=int(input("enter your pin: "))
#     correct_pin=1234
#     if(user_pin==correct_pin):
#         print("transaction successful")
#         print("remaining balance:",account_balance-withdrawal_amount)
#     else:
#         print("incorrect PIN")    
# else:
#     print("insufficient balance")

# # #QUESTION 3- LOGIN SYSTEM
# correct_username = "admin"
# correct_password = "python123"
# username= input("enter username: ")
# username=username.lower()
# if(username==correct_username):
#     print("valid username")
#     user_password=input("enter password: ")
#     user_password=user_password.lower()
#     if(user_password==correct_password):
#         print("correct password")
#         user_role=input("kindly enter your role: ")
#         user_role=user_role.lower()
#         if(user_role=="admin"):
#             print("welcome admin")
#         elif(user_role=="teacher"):
#             print("welcome teacher")
#         elif(user_role=="student"):
#             print("welcome student")
#         else:
#             print("unknown role")            
#     else:
#         print("invalid password","\nplease enter the correct password to login")        
# else:
#     print("invalid username","\nplease enter the correct username to login")         

# # QUESTION 4- LARGEST NUMBER
# first_number=int(input("enter the first number: "))
# second_number=int(input("enter the second number: "))
# third_number=int(input("enter the third number: "))
# print("the first number is",first_number)
# print("the second number is",second_number)
# print("the third number is",third_number)
# if(first_number>second_number and first_number>third_number):
#     print("the first number is largest which is",first_number)
# elif(second_number>first_number and second_number>third_number):
#     print("the second number is largest which is",first_number)
# elif(third_number>first_number and third_number>second_number):
#     print("the third number is largest which is",first_number)
# else:
#     print("the two numbers are the same")

#QUESTION 5- TICKET PRICING
# print("welocme to the ticket pricing system")
# user_age = int(input("enter age: "))
# if(user_age<5):
#     print("FREE")
# elif(user_age>=5 and user_age<=12):
#     print("RS 200")    
# elif(user_age>=13 and user_age<=59):
#     print("RS 500")
# elif(user_age>=60):
#     print("RS 300")
# vip_check = input("VIP? (YES/NO) ")
# vip_check=vip_check.lower()
# if(vip_check=="yes"):
#     print("rs 300 will be added to your ticket price")
#     if(user_age>=5 and user_age<=12):
#         print("RS",200+300)
#     elif(user_age<5):
#         print("RS",0+300)    
#     elif(user_age>=13 and user_age<=59):
#         print("RS",500+300)
#     elif(user_age>=60):
#         print("RS",300+300)
#     else:
#         print("invalid input") 
# else:
#     print("you can go with the previous price. thanks for you patience.")  

#QUESTION 6- UNIVERSITY ADMISSION 
# percentage_user = float(input("enter your previous percentage: "))
# if(percentage_user>=60.0):
#     print("congratulations, you are eligible")
#     semester = input("kindly enter your semester (1st 2nd 3rd 4th): ")
#     semester= semester.lower()
#     if(semester=="1st"):
#         print("eligible for admission")
#     elif(semester=="2nd"):
#         print("eligible for admission")    
#     elif(semester=="3rd"):
#         print("eligible for admission")    
#     elif(semester=="4th"):
#         print("eligible for internship")    
#     else:
#         print("invalid input")
# else:
#     print("not eligible")                   

#QUESTION 7- EVEN/ODD + POSITIVE/NEGATIVE
# number_from_user = int(input("enter the number: "))
# print("the number you entered is:",number_from_user)
# if(number_from_user>0):
#     print("the number is positive")
#     if(number_from_user%2==0):
#         print("the number is positive and even")
#     else:
#         print("the number is positive and odd")        
# elif(number_from_user<0):
#     print("the number is negative")
#     if(number_from_user%2==0):
#         print("the number is negative and even")
#     else:
#         print("the number is negative and odd")
# else:
#     print("the number is zero") 
           
#QUESTION 8- RESTAURANT BILL
# bill_amount = float(input("enter your bill amount: "))
# print("the bill you entered is",bill_amount,"\nkindly check")
# if(bill_amount>=1000 and bill_amount<=4999):
#     print("10 percent discount is given to you")
#     t1=bill_amount*10/100
#     print("your new bill is",t1)
#     member_discount= input("member? (yes/no): ")
#     member_discount=member_discount.lower()
#     if(member_discount=="yes"):
#         print("you are given extra 5 percent discount")
#         print("your final bill is",t1*5/100)
#     else:
#        print("no extr discount")    
# elif(bill_amount>=5000 and bill_amount<=9999):
#     print("20 percent discount is given to you")
#     t2=bill_amount*20/100
#     print("you new bill is",t2)
#     member_discount= input("member? (yes/no): ")
#     member_discount=member_discount.lower()
#     if(member_discount=="yes"):
#         print("you are given extra 5 percent discount")
#         print("your final bill is",t2*5/100)
#     else:
#        print("no extra discount")    
# elif(bill_amount>= 10000):
#     print("30 percent discount is given to you")
#     t3=bill_amount*30/100
#     print("you new bill is",t3)
#     member_discount= input("member? (yes/no): ")
#     member_discount=member_discount.lower()
#     if(member_discount=="yes"):
#         print("you are given extra 5 percent discount")
#         print("your final bill is",t3*5/100)
#     else:
#        print("no extra discount")    
# else:
#     print("no discount")

#QUESTION 9- PASSWORD STRENGTH CHECKER
# password_user= input("enter the password: ")
# if(len(password_user)<8):
#     print("the password you entered is weak")
# elif(len(password_user)>=8):
#     print("now you have entered the correct password")
#     if(password_user==password_user.isdigit()):
#         print("medium password")    
#     elif(password_user==password_user.isalnum()):
#         print("strong password")
#     else:
#         print("not right") 
# else:
#     print("invalid password")        

#QUESTION 10- MINI QUIZ GAME
# question1 = input("What is the capital of Pakistan? \n")
# question1=question1.lower()
# if(question1=="islamabad"):
#     print("let us move to question 2")
#     question2 = input("2+2= \n")
#     question2=question2.lower()
#     if(question1=="islamabad" and question2!="4"):
#         print("first answer correct,second wrong")
#     elif(question1=="islamabad" and question2=="4"):
#         print("congratulations")
#     else:
#         print("invalid input") 
# else:
#     print("quiz over")    
    
#CHALLENGE ATM MACHINE PROJECT
# username=input("enter your username: ").lower()
# correct_username="nimra123"
# password=input("enter your password: ")
# correct_password="123an"
# balance=float(input("enter your current balance: "))
# if(username==correct_username and password==correct_password):
#     print("\nMENU\n","1.CHECK BALANCE\n","2.DEPOSIT\n","3.WITHDRAW\n","4.EXIT\n")
#     choice=input("enter your choice: ")
#     if(choice=="1"):
#         print("your balance is",balance)
#     elif(choice=="2"):
#         print("deposit...")
#         deposit_amount=float(input("enter the amount to deposit: "))
#         print("the amount you deposited is:",deposit_amount)
#         if(deposit_amount>=0):
#             print("right amount to deposit.")
#             print("your final balance is:",balance+deposit_amount)
#         else:
#             print("negative amount can not be deposited.")    
#     elif(choice=="3"):
#         print("withdraw...")
#         withdraw_amount=float(input("enter the amount to withdraw: "))
#         print("the amount you withdraw is:",withdraw_amount)
#         if(withdraw_amount>balance):
#             print("error")
#         else:
#             print("right amount to withdraw")    
#             print("your final balance is:",balance-withdraw_amount)
#     elif(choice=="4"):
#         print("exit")    
#     else:
#         print("invalid input")    
# elif(username!=correct_username and password!=correct_password):
#     print("exit")
# elif(username==correct_username and password!=correct_password):
#     print("exit\n","username is correct but password is wrong","\nenter correct password")
# elif(username!=correct_username and password==correct_password):
#     print("exit\n","password is correct but username is wrong","\nenter correct username")
# else:
#     print("invalid input")    
         
#codewithharry exercise GOOD MORNING SIR:
import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp=time.strftime('%H')
# print(timestamp)
# timestamp=time.strftime('%M')
# print(timestamp)
# timestamp=time.strftime('%S')
# print(timestamp)

print("game starting in: " )
print("3")
time.sleep(3)
print("2")
time.sleep(3)
print("1")
time.sleep(3)
print("GO")

