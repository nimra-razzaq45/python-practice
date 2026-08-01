# #simple if/else
# age = int(input("enter your age: "))
# print("your age is",age)
# if(age>=18):
#     print("you can drive..")
# else:
#     print("you can not drive..") 

# #elif
# appleprice = 190
# budget = 200
# if (budget - appleprice > 50):
#     print("alexa, add 1 kg apples to the cart..")
# elif (budget-appleprice > 20):
#     print("it is okay. u can buy..")    
# else:
#     print("alexa, do not add apples to the cart..")    

# #example
# num1 = int(input('enter the number: '))
# if(num1<0):
#     print("the number is negative..")
# elif(num1==0):
#     print("the number is zero..")
# elif(num1==999):
#     print("the number is special..") 
# else:
#     print("the number is positive..") 

#nested if/else
# #ek if k andar ek ur if that is nested
# num = 245
# if(num<0):
#     print("number is negative..")
# elif(num>0):
#     if(num<=10):
#         print("number is between 1-10..")
#     elif(num>10 and num<=20):
#         print("number is between 11-20")        
#     else:
#         print("number is greater than 20..")
# else:
#     print("number is zero..")
# print("i am happy now..")

#claude examples
#AND operator ma dono conditions true honi chahiye
age = 15
has_ticket = True
if (age>=18 and has_ticket):
    print("entry allowed..","\nenjoy your movie :)")
else:
    print("not allowed..")

#OR operator ma koi ek true ho to kafi hai
is_weekend = False
is_holiday = False 
if(is_weekend or is_holiday):
    print("no work today")
else:
    print("go to work")

#NOT operator condition ko ulta kr deta hai
is_raining = False
if (not is_raining):
    print("let's go outside.")
else:
    print("stay inside.")    
