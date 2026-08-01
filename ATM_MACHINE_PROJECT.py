#CHALLENGE ATM MACHINE PROJECT
username=input("enter your username: ").lower()
correct_username="nimra123"
password=input("enter your password: ")
correct_password="123an"
balance=float(input("enter your current balance: "))
if(username==correct_username and password==correct_password):
    print("\nMENU\n","1.CHECK BALANCE\n","2.DEPOSIT\n","3.WITHDRAW\n","4.EXIT\n")
    choice=input("enter your choice: ")
    if(choice=="1"):
        print("your balance is",balance)
    elif(choice=="2"):
        print("deposit...")
        deposit_amount=float(input("enter the amount to deposit: "))
        print("the amount you deposited is:",deposit_amount)
        if(deposit_amount>=0):
            print("right amount to deposit.")
            print("your final balance is:",balance+deposit_amount)
        else:
            print("negative amount can not be deposited.")    
    elif(choice=="3"):
        print("withdraw...")
        withdraw_amount=float(input("enter the amount to withdraw: "))
        print("the amount you withdraw is:",withdraw_amount)
        if(withdraw_amount>balance):
            print("error")
        else:
            print("right amount to withdraw")    
            print("your final balance is:",balance-withdraw_amount)
    elif(choice=="4"):
        print("exit")    
    else:
        print("invalid input")    
elif(username!=correct_username and password!=correct_password):
    print("exit")
elif(username==correct_username and password!=correct_password):
    print("exit\n","username is correct but password is wrong","\nenter correct password")
elif(username!=correct_username and password==correct_password):
    print("exit\n","password is correct but username is wrong","\nenter correct username")
else:
    print("invalid input")    
         