# QUESTION 4- LARGEST NUMBER
first_number=int(input("enter the first number: "))
second_number=int(input("enter the second number: "))
third_number=int(input("enter the third number: "))
print("the first number is",first_number)
print("the second number is",second_number)
print("the third number is",third_number)
if(first_number>second_number and first_number>third_number):
    print("the first number is largest which is",first_number)
elif(second_number>first_number and second_number>third_number):
    print("the second number is largest which is",first_number)
elif(third_number>first_number and third_number>second_number):
    print("the third number is largest which is",first_number)
else:
    print("the two numbers are the same")