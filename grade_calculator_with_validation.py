# #q2 grade calculator with validation
marks=int(input("enter marks between 0-100: "))
is_fail = True
if (marks<0 or marks>100) :
    print("invalid marks")
elif (marks>0 or marks<100):
    print("valid marks")
    if(marks>=90):
        print("A+",not is_fail)
    elif(marks>=80 and marks<=89):
        print("A",not is_fail)
    elif(marks>=70 and marks<=79):
        print("B",not is_fail)
    elif(marks>=60 and marks<=69):
        print("C",not is_fail)
    else:
        print("Fail", is_fail)    
else:
    print("invalid")