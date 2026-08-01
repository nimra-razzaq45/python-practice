#question3 email validator
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