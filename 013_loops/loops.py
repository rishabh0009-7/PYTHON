#loops in python 
#1. Counting Positive Numbers
#Problem: Given a list of numbers, count how many are positive.
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# positive_count = 0
# for i in numbers :
#     if i >0:
#         positive_count+= 1

# print("final count of positive number is ",positive_count)


#2. Sum of Even Numbers
#Problem: Calculate the sum of even numbers up to a given number n.
# n = int (input ("enter the number "))
# sum_even= 0 

# for i in range(1,n+1):
#     if i %2==0:
#         sum_even = sum_even +1
# print("sum of even number is ", sum_even)


#3. Multiplication Table Printer
#Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

# number = int (input ("enter the number "))

# for i in range (1,11):
#     if i==5:
#         continue
#     print(number, 'x',i, '=', number*i)


#4. Reverse a String
#Problem: Reverse a string using a loop

# input_str = "python"
# reverse_str= ""
# for char in input_str:
#     reverse_str= char+ reverse_str


# print(reverse_str)
 
#5. Find the First Non-Repeated Character
#Problem: Given a string, find the first non-repeated character.
#non repeated means ki vo ek hi baar ho 

# input_str= "teeterhbsdt"

# for char in input_str:
#     if input_str.count (char)==1:
#         print("char is :", char)
#         break  #coz we only want one repeated character i.e first


#6. Factorial Calculator
#Problem: Compute the factorial of a number using a while loop.
#factorial = 5*4*3*2*1 # 5 can be written as 5*1  and 4 as 4*1

# number= 5
# factorial= 1

# while number>0:
#     factorial = factorial * number 
#     number = number -1
# print("factorial", factorial)

#7. Validate Input
#Problem: Keep asking the user for input until they enter a number between 1 and 10.


# while True :
#     number = int (input("enter the value b/w 1 and 10 "))
#     if 1<=number <=10:
#         print("thx")
#         break
#     else :
#         print("invalid number")



  #  8. Prime Number Checker
#Problem: Check if a number is prime.

# number = 29 
# is_prime = False 

# if number >1:
#     for i in range (2, number ):
#         if i %2== 0:
#             is_prime = False 
#             break
# print(is_prime)
    


#9-. List Uniqueness Checker
#Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.


# items = ["apple", "banana", "orange", "apple", "mango"]
# # we will use set becoz set apna nadar na unique element shi rakhta hai
# unique_item = set()
# # ek ek kar loop chalayega aur item ko uniwue walaa mai daal dega aur agar vo repeat kara to duplicate 

# for item in items:
#     if item in unique_item :
#         print("duplicate", item)
#         break
#     unique_item.add(item)

#10. Exponential Backoff
#Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

import time
wait_time = 1 
max_tries = 5 
attempts = 0
while attempts< max_tries:
    print("attempts",attempts +1, "wait time " ,wait_time)
    time.sleep(wait_time) # itni der kaam nhi kar raha to timer band rehna chahiye isliye ye kara 
    wait_time*=2
    attempts+=1


 