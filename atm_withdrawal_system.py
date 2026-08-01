#q3 atm withdrawal system
user_account = float(input("enter your account balance: "))
withdraw_amount = float(input("how much you want to withdraw: "))
if(withdraw_amount>user_account):
    print("insufficient balance")     
elif(withdraw_amount<=0):
    print("invalid amount")  
elif(withdraw_amount<=user_account and withdraw_amount>100):
    print("withdrawal successful","\nyour new balance is",user_account-withdraw_amount)
elif(withdraw_amount<=user_account and withdraw_amount<100):
    print("minimum withdrawal amount is 100") 
print("thankyou for your patience")  