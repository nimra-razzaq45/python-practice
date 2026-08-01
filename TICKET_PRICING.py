#QUESTION 5- TICKET PRICING
print("welocme to the ticket pricing system")
user_age = int(input("enter age: "))
if(user_age<5):
    print("FREE")
elif(user_age>=5 and user_age<=12):
    print("RS 200")    
elif(user_age>=13 and user_age<=59):
    print("RS 500")
elif(user_age>=60):
    print("RS 300")
vip_check = input("VIP? (YES/NO) ")
vip_check=vip_check.lower()
if(vip_check=="yes"):
    print("rs 300 will be added to your ticket price")
    if(user_age>=5 and user_age<=12):
        print("RS",200+300)
    elif(user_age<5):
        print("RS",0+300)    
    elif(user_age>=13 and user_age<=59):
        print("RS",500+300)
    elif(user_age>=60):
        print("RS",300+300)
    else:
        print("invalid input") 
else:
    print("you can go with the previous price. thanks for you patience.") 