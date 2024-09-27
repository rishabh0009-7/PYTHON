#tuple in python 
#list and tuple are same but list is mutable and tuple is immutable
tea_type = ("black", "masala", "green")
print(tea_type)
print(tea_type[0])
print(tea_type[-1])
print(tea_type[1:3])



#updation not possible  (immutable hai)
# tea_type[0] = "lemon" #this is not possible 

#rest all are same as list

(black,masala,green)= tea_type
print(black)
print(type(tea_type))

