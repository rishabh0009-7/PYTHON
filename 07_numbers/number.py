# #numbers - in python number  is a group of object not a single object 


# #operations - we can do any kind of operations add .sub.mul.div

# x= 2
# y=3
# z=4

# # print(x+y)

# # # we can also typecast

# # print (int(2.23)) #2

# # #we can add 2 strings
# # print ('chai'+ 'code')

# # print (x,y,z)

# # #some more operations
# # print (z**4)

# # print(2**100)

# #comparisons
# # print (1<2)
# # print (5.0==5.0)


# # print (4.0 != 5.0)
# # print ((x<y) and (y<z)) 

# # print (1== 2<3) # here  1 is  considered as  true
 

# #  #in python sometimes we have to import other library to use fnctions 
# # import math

# # #1- math.floor ---> gives closest number below value 
# # print (math.floor(3.5))  #3
# # print (math.floor(-4.9))  #-5

# # #2- math.trunc ---> this will take you towards 0  nearest value 
# # print(math.trunc(3.8)) #3
# # print(math.trunc(-3.8)) #-3

# # #in python there s number precision (chahe kitni bhi badi value ho kar dega solve )
# # print(99999999999999999999999999+1)


# # print(2+1j) # here j represents  imaginary numbers

# # #octal literals (starts with 0o)
# # print(0o20) #16

# # #hexal literals(0x)
# # print(0xff) #255

# # #binary literals(0b)
# # print(0b1000) #8

# # # to convert numbers into  octal ,hex .binary
# # print(oct(64)) #0o100
# # print(hex(64))#0x40
# # print(bin(64)) #0b1000000

# # #another way 
# # print(int ('64',8)) # iska matlab hai ki 64 ka octal value dedo i.e 52


# #random library 
# import random
# print(random.random()) # this will give random numbers 

# # if u want random numbersin specific range 
# print(random.randint(1,100))

# l1= ['lemon', 'chai', 'ginger', 'mint']
# print(random.choice(l1))

# print(random.shuffle(l1))

# #decimal precision in python is very problematic
# print(0.1+0.1+0.1 - 0.3) # this should be 0 but python gives a weird value 

# so for decimal we have to import decimal 
# from Decimal import Decimal  

# print(Decimal('0.1') +  Decimal('0.1') +  Decimal('0.1') - Decimal('0.3'))

 #sets 
setone= {1,2,3,4}
print(setone &{1,3}) #intersection
print(setone |{1,3}) #union
print(setone -{1,2,3,4})  # ye aayega set() not this set{} becoz ye dictionary hojayega 


#boolean type 
print(type (True ))
#true==1 and false ==0 
print(True +4) #5