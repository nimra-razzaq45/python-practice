# # #question1 username generator
# name = input("enter your full name: ")
# name = (name.lower())
# print("lowercase:",name)
# name = (name.replace(" ",""))
# print("name after replace:",name)
# birth_year = int(input("enter your birth year: "))
# birth_year = str(birth_year)
# user_name = (name + birth_year)
# print("your username is:",user_name)
# print("length:",len(user_name))
# is_long_username = len(user_name) > 15
# print("is username longer than 15:",is_long_username)
# print(user_name.isalnum())

# #question2 palindrome checker(without loop)
# word = input("write any small word: ")
# print("the word given by user:",word)
# reverse_word = word[::-1]
# print("reverse word:",reverse_word)
# word=word.lower()
# reverse_word=reverse_word.lower()
# is_palindrome = word == reverse_word
# print("is palindrome:",is_palindrome)
# vowels_a = (word.count("a"))
# vowels_e = (word.count("e"))
# vowels_i = (word.count("i"))
# vowels_o = (word.count("o"))
# vowels_u = (word.count("u"))
# print("a","e","i","o","u")
# print(vowels_a,vowels_e,vowels_i,vowels_o,vowels_u)
# total_vowels = int(vowels_a+vowels_e+vowels_i+vowels_o+vowels_u) 
# print("total vowels=",total_vowels)   

# #question3 email validator
user_email = input("write your email address: ")
print("the email address given by user is :",user_email)
print("contains @:","@" in user_email)
print("valid ending",user_email.endswith(".com"))
print("after split:",user_email.split("@"))
result = user_email.split("@")
username = result[0]
domain = result[1]
print("username:",result[0])
print("domain:",result[1])



