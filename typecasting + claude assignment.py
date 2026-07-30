name = "nimra"
age = 21
cgpa = 3.6
is_topper = cgpa >= 3.5

print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_topper))

print("----------")

info = name + " is " + str(age) + " years old."
print(info)

print("-----------")

cgpa_int = int(cgpa)
print("cgpa as integer is: ", cgpa_int)

print("------------")

print("is topper: ", is_topper)

x = 10 > 5
y = 10 == 5
z = "abc" == "abc"

print(type(x),x)
print(type(y),y)
print(type(z),z)

a="1.5"
b="5"
print(float(a)+float(b))

g = 3.14
g_int = int(g)
print(g_int)