#QUESTION 1- STUDENT GRADE SYSTEM
marks = int(input("enter your marks: "))
if(marks>=0 and marks<=100):
    print("valid marks") 
    if(marks>=90):
        print("A+")
    elif(marks>=80):
        print("A")
    elif(marks>=70):
        print("B")
    elif(marks>=60):
        print("C")
    elif(marks>=50):
        print("D")
    else:
        print("fail")    
else:
    print("invalid marks")