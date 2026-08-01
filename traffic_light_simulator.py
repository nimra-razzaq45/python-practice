#q5 traffic light simulator
user_color = input("enter a color e.g red yellow green: ")
print("the color you entered: ",user_color)
user_color=user_color.upper()
if(user_color=="RED"):
    print("STOP")
elif(user_color=="YELLOW"):
    print("GET READY")
elif(user_color=="GREEN"):
    print("GO")
else:
    print("invalid color. only red green yellow are allowed :)")