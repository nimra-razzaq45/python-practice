#pract1
print("\nwelcome to the restaurant bill splitter program\n")
total = float(input("enter the total bill : "))
print("total bill :",total)
total_friends = int(input("enter the number of total friends : "))
print("total friends : ",total_friends)
each_person_pay = (total/total_friends)
print("each person will pay : ",each_person_pay)
even_split = total%total_friends == 0
print("can be split evenly : ",even_split)