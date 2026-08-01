#q6 ride fare calculator (uber/careem type)
distance = float(input("enter the distance: "))
time = input("enter the time (day/night): ")
time=time.upper()
rain = input("is there rain? (yes/no) ")
rain=rain.upper()
print("fare rules: ")
base_fare = 50 + (distance * 20)
if(time=="NIGHT"):
    print("fare with 20% extra: ",base_fare * 20)
elif(rain=="YES"):
    print("we will charge extra.")
    if(time=="DAY" or time=="NIGHT"):
        print("we charge extra 100 RS",base_fare+100)