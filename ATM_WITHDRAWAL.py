# #QUESTION 2- ATM WITHDRAWAL 
account_balance= int(50000)
withdrawal_amount= int(input("enter the amount to withdraw: "))
if(withdrawal_amount<=account_balance):
    print("the amount you want to withdraw is:",withdrawal_amount)
    user_pin=int(input("enter your pin: "))
    correct_pin=1234
    if(user_pin==correct_pin):
        print("transaction successful")
        print("remaining balance:",account_balance-withdrawal_amount)
    else:
        print("incorrect PIN")    
else:
    print("insufficient balance")