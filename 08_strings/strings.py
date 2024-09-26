# strings in python 
a= "   masala chai   "
print(a)

# # string slicing 
# firstch = a[0]
# print(firstch)

# slicing_chai = a[0:6]  #masal
# print(slicing_chai)

# num_list = "0123456789"
# print(num_list[:]) #0123456789
# print(num_list[3:]) #3456789
# print(num_list[:7]) #0123456
# print(num_list[0:7:2]) #0246


#string methods 
print (a.lower())
print (a.upper())
print (a.strip ()) # removes extra sapces from start and end 
print (a.replace("masala", "ginger")) # this will replace masala with ginger


b= "lemon,ginger,masala,mint"

# to convert this into a list
print (b.split(","))


print(a.find("chai"))

# agar koi cheez exist nhi karti to ye -1 dega output
