#question1 username generator
name = input("enter your full name: ")
name = (name.lower())
print("lowercase:",name)
name = (name.replace(" ",""))
print("name after replace:",name)
birth_year = int(input("enter your birth year: "))
birth_year = str(birth_year)
user_name = (name + birth_year)
print("your username is:",user_name)
print("length:",len(user_name))
is_long_username = len(user_name) > 15
print("is username longer than 15:",is_long_username)
print(user_name.isalnum())