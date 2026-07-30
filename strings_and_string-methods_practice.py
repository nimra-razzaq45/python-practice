# # #string prac1
# a = '''hi
# i am nimra
# how are you
# hope u are good and fine'''


name = "arham"
for letters in name:
    print(letters)
    
# #string slicing
# #python string indexing/slicing ma last wale index ko nai leta is liye [0:4] krne pr we only get harr
# name = "harry"
# print(name[0:4])    
# #negative slicing
# name = "PYTHON"
# print(name[-5])
# #ek ur tarkia
# fruit = "MANGO"
# print(fruit[:-4])
# print(fruit[-4:])
# #reverse indexing + step (syntax = [start:stop:step]) step mtlb itne point pr jana hai 2 step mtlb 0 sy 2 pr jana
# fruit1 = "BANANA"
# print(fruit1[::-1])
# #forward step
# print(fruit1[:]) #pura word print krne k liye jese banana
# print(fruit1[0:9:3]) #mtlb 3 step move kro

# #string length
# fruit2 = "apple"
# len1 = len(fruit2)
# print("length of word apple is",len1,"letters...")

# #harry ka easy example of string slicing
# print("\n\nHARRY KA EXAMPLE\n\n")
fruit3 = "Mango"
mangolen = len(fruit3)
print(mangolen)
print(fruit3[:2])
# print(fruit3[0:4]) #include 0 but not 4
# print(fruit3[1:4]) #include 1 but not 4
# print(fruit3[:5])
# print(fruit3[0:-3])
# print(fruit3[:len(fruit3)-3])
# print(fruit3[-1:len(fruit3)-3]) #ya error de ga not possible bcz we get (4:2) not applicable
# print(fruit[-3:-1]) #ultimately ap len(fruit3 ur -1 kro gy you will get 5-3= 2) and (5-1=4) to (2:4) 

#quick quiz
# print("\nHARRY KA QUIZ\n")
# nm="harry"
# print("the answer we get is",nm[-4:-2],"\nhurray! you did great :)")

#string methods
#remember strings are immutable
name = "harry"
print(len(name))
#upper_case and lower_case
print(name.upper(),name.lower()) #capital ya small letters k liye
#strip()
n1 = " nimra razzaq "
print("beforen strip:",n1,"after strip:",n1.strip()) #removes white spaces
#rstrip()
n2="!!!nimra.........."
print("after rstrip:",n2.rstrip(".")) #trailing characters remove only, not leading
#replace()
n3="harry!!!!!!!harry....harry"
print(n3.replace("harry","johnn")) #replace kr deta hai all occurences ko
#split()
n4="111harry 444nimra 246arham 899ayesha 221sara"
print(n4.split(" ")) #"list bana deta hai"
#capitalize()
blogheading = "introduction tO jS"
print(blogheading.capitalize() ) #pehla letter capital UR AGR KOI CAPITAL REH JAE TO USKO B SAHI KR DETA HAI
#center()
print(blogheading.center(50))   #heading ko center ma lane k liye
print(len(blogheading))
print(len(blogheading.center(50)))
#count()
print(n3.count("harry")) #koi word kitni dafa aya usko count krne k liye
#endswith()
print(blogheading.endswith("jS"))
print(blogheading.endswith("on",4,12)) #check kr k batae ga k string is word ya letter sy end ho rhi hai (bool dega true/false)
#find()
print(blogheading.find("to")) #agr kuch exist nai kry ga to ya -1 dega ur agr mil gaya to index return
#index()
print(blogheading.index("tO")) #agr na ho to error dekar exit program
