print("\nwelcome to number analyzer!\n")
user_number = int(input("enter the desired number : "))
is_even = user_number%2 == 0
print("is the number even? ",is_even)
is_greater = user_number > 10
print("is the number greater than 10? ",is_greater)
string_user_number = str(user_number)
print("your number is "+string_user_number,"\nthe previous data type of number is:",type(user_number),"\nthe new data type of number is:",type(string_user_number))
user_second_number = int(input("enter the second desired number to calculate modulus : "))
modulus_check = user_number%user_second_number == 0
print("is the number fully divided? ",modulus_check) 

