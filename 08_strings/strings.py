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


print (a.count("chai"))

#we can add variables inside a variableusing{}  and format method 
#  ex-
chai_type = "masala"
quantity = 2
order = "i ordered {} cups of {} chai "

print(order.format(quantity,chai_type))

# agar join karna hai  multiple strings ko 
chai_variety = ["lemon", "masala", "ginger "]
print(",".join(chai_variety))


print(len(a))

# we can also use loops in string 
for i in a :
    print(i )


#rawstring - jaisa likha hai waisa hi print ho jayaa 

chai= r"masala\nchai"
print(chai)  #masala\nchai


#we can ask something from python also 

b= "masala chai "
print("masala" in chai ) # true 
