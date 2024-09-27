#dictionary in python - key value pair 
# chai_types = {
#     "masala": "spicy",
#     "ginger": "zesty",
#     "green": "mild",

# }
# print(chai_types)
#methods
#get method to  get value using key 
# print(chai_types.get("masala")) 

# #updation
# chai_types["green"]= "fresh"
# chai_types["earlgrey"]= "citrus"


# how to print
# for i  in chai_types:
#     print(i)  # this will print key

# for i  in chai_types:
#     print(i,chai_types[i]) #this will print both keys and value

# #better way 
# for key,value in chai_types.items():
#     print(key,value)

# #condns
# if "masala" in chai_types :
#     print("i have masala chai ")

#pop 
# chai_types.pop("ginger ") #dict mai btana  padta hai  kya pop karna hai 
#pop item - ye  last wala remove karta hai
# print(chai_types.popitem())
 

 #u can also create copy in dict just like list

# chai_typesnew= chai_types.copy()

#multiple dictionaries 
tea_shop= {
    "Chai":{"masala":"spicy","ginger": "zesty",} ,
    "Tea":{"green":"mild",  "black":"strong" }
}

print(tea_shop["Chai"]["ginger"])

#dict comprehension 

squared_num= {x:x**2 for x in range (6) }

#clear method 
print(squared_num.clear())


#construct a new dictionary using a list and   single variable 
#dict.from
keys=["masala", "ginger ","lemon"]

default_value= "delicious"

dictionary = dict.fromkeys(keys,default_value)
print(dictionary)

