#QUESTION 8- RESTAURANT BILL
bill_amount = float(input("enter your bill amount: "))
print("the bill you entered is",bill_amount,"\nkindly check")
if(bill_amount>=1000 and bill_amount<=4999):
    print("10 percent discount is given to you")
    t1=bill_amount*10/100
    print("your new bill is",t1)
    member_discount= input("member? (yes/no): ")
    member_discount=member_discount.lower()
    if(member_discount=="yes"):
        print("you are given extra 5 percent discount")
        print("your final bill is",t1*5/100)
    else:
       print("no extr discount")    
elif(bill_amount>=5000 and bill_amount<=9999):
    print("20 percent discount is given to you")
    t2=bill_amount*20/100
    print("you new bill is",t2)
    member_discount= input("member? (yes/no): ")
    member_discount=member_discount.lower()
    if(member_discount=="yes"):
        print("you are given extra 5 percent discount")
        print("your final bill is",t2*5/100)
    else:
       print("no extra discount")    
elif(bill_amount>= 10000):
    print("30 percent discount is given to you")
    t3=bill_amount*30/100
    print("you new bill is",t3)
    member_discount= input("member? (yes/no): ")
    member_discount=member_discount.lower()
    if(member_discount=="yes"):
        print("you are given extra 5 percent discount")
        print("your final bill is",t3*5/100)
    else:
       print("no extra discount")    
else:
    print("no discount")