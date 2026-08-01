#pract2
print("electricity bill checker")
units_consumed = int(input("enter the units consumed : "))
print("total units consumed : ",units_consumed)
rate_per_unit = int(25)
total_bill = (units_consumed*25)
print("your electricity bill is Rs ",total_bill)
is_high_bill = total_bill > 5000
print("high alert bill : ",is_high_bill)
unit_value_check = units_consumed%2 == 0
print("are units even? ",unit_value_check)