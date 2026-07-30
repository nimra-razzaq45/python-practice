name = " pyTHon programming........."
# print(name.upper()) #all capital letter
# print(name.lower()) #all small
# print(name.title()) #sary words k first letter big
# print(name.capitalize()) #sirf first word ka first letter big
# print(name.strip()) #white spaces remove
# # print(name.rstrip(".")) #trailing characters remove jese . ! etc
# # print(name.replace("pyTHon","c++")) #kisi word ko agr change krna ho
# print(name.find("THon")) #kisi b word k kisi letter ka index batata hai
# # print(name.find("z")) #agr na mile to -1 return
# print(name.index("z")) #same as find lakin ya error deta hai jab koi letter na mile
# print(name.count("p")) #koi letter string ma kitni bar aya hai
# print(name.startswith(" ")) #check krta hai string kis sy start hui. true ya false
# print(name.endswith(".")) #check krta hai end kis pr ho rhi. true ya false
# n2 = "nimra arham"
# print(n2.split()) #list bana deta hai 
# n3=["mango","apple","banana","orange","apricot","pomegranate","avacardo"]
# print(" ".join(n3)) #split ka opposite hai ya. list ko join kr deta hai
# print(n2.isalpha()) #again a bool check krne k liye k string ma sirf letters hain ya nai --> true if numbers the --> false
# n4="1234554"
# print(n4.isdigit())
# n5="nimra123"
# print(n5.isalnum()) #numbers + letters --> true if any space or character --> false
# n6="     "
# print(n6.isspace()) #check krta hai k sirf space hi hai
# print("HELLO".isupper())
# print("hello".islower())
# print(name.swapcase()) #agr bary letter wo small kr deta hai ur agr small to wo bary kr deta hai 
# print(n2.center(50)) #heading ko center ma krne k liye
# print(n2.ljust(22,"-")) #heading ko left side krne k liye
# print(n2.rjust(22,"-")) #heading ko right side krne k liye
print("7".zfill(5))
print("'''''''hello".lstrip("'"))
print("hello.........".rstrip("."))
print("world" in "hello world") #in jo hai wo ek keyword hai (technically it is an operator, not a method)
print("my name is {}".format("nimra"))
p1 = "my name is nimra\n"
print(p1.isprintable()) #ya check krne k liye hota hai k koi print na hone wala character b hai jese \n is not printable
t = "Intro To Chemistry"
print(t.istitle())

#practice questions chatgpt
# #q1
# name = input("enter your name : ")
# print("name in uppercase is:",name.upper())
# #q2
# city = input("enter your city : ")
# print("your city in lowercase is:",city.lower())
# #q3
# fullname = input("enter your full name : ")
# print("your full name is:",fullname.title())
# #q4
# sentence = "i love java"
# sentence = sentence.title()
# print(sentence.replace("java","python"))
# #q5
# word = "Programming"
# print(len(word))
# print("the letter g comes",word.count("g"),"times")
# #q6
# user_word = input("type any word: ")
# print(user_word.startswith("p"))
# print(user_word.endswith("n"))

#practice questions
#q1
# name = input("write you full name: ")
# print("your full name using split is:",name.split())
# #q2
# languages=["python","java","c++"]
# print(" | ".join(languages))
# #q3
# word = input("write any word: ")
# print("we get the following results..","\nletter check: ",word.isalpha(),"\ndigit check: ",word.isdigit(),"\nboth check: ",word.isalnum())
# #q4
# text = input("you can write any text here..\n")
# print("text after swapcase is: ",text.swapcase())
# #q5
# myname = "nimra razzaq"
# print("center: ",myname.center(50))
# print("left: ",myname.ljust(50,"-"))
# print("right: ",myname.rjust(50,"-"))

#//////len is a function not a method/////


