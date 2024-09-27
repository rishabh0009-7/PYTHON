#list in python  or array in other languages 

tea_variety = ["blaxk ", "green", "oolang", "white "]
print(tea_variety)
#list slicing and dicing
print(tea_variety[0])

print(tea_variety[1:3])
print(tea_variety[ :2])
print(tea_variety[2:])

 #updation
tea_variety[3]= "herbal"
print(tea_variety)

print(tea_variety[1:1]) # [] becoz 1 excluded hai
#basic loops
for tea in tea_variety:
    print(tea,end="-")

#methods 
tea_variety.append("chai")# adds at the end
print(tea_variety)
print(tea_variety.pop()) #removes last value 

print(tea_variety.remove("green")) #u can remove any specific value 

tea_variety.insert(1,"pink") #insert value at specific position
print(tea_variety)

#we can copy any variable with different memory location no reference this time 
tea_variety_new = tea_variety.copy()
print(tea_variety_new)  # isme alag memory mai banega 


tea_variety_new = tea_variety
print(tea_variety_new)  # isme same  memory mai banega  same reference 

#list comprehension = we can also do comprehnsion (calculation inside list)

#range (10) means 0-10

squared_nums= [x**2 for x in range(10)]
print(squared_nums) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squared_nums= [y**3 for  y in range(10)]
print(squared_nums)  #[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]



