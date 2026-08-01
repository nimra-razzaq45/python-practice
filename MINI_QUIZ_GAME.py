#QUESTION 10- MINI QUIZ GAME
question1 = input("What is the capital of Pakistan? \n")
question1=question1.lower()
if(question1=="islamabad"):
    print("let us move to question 2")
    question2 = input("2+2= \n")
    question2=question2.lower()
    if(question1=="islamabad" and question2!="4"):
        print("first answer correct,second wrong")
    elif(question1=="islamabad" and question2=="4"):
        print("congratulations")
    else:
        print("invalid input") 
else:
    print("quiz over") 