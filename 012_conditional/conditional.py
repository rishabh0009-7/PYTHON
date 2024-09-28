# # 1- age group  categorization
# #classify a person's age group: child (<13),teenager(13-19),adult (20-59),senior(60+)

# age= int(input("enter your age ")) 
# if age<13:
#     print("child ")
# elif age>13 &age <=19:  
#     print("teenager")
# elif age >20 and age<=59 : 
#     print("adult")
# elif age >=60:   45
#     print("seniors")

# #method 2
# age= int(input("enter your age ")) 
# if age<13:
#     print("child ")
# elif age <20:  #age<20
#     print("teenager")
# elif age<60 : #age<60
#     print("adult")
# else:   #only else:
#     print("seniors")

#2-movie ticket pricing 
# problem:movie tickets are priced based on age : $12 for adults(18 and over ),$8 for children .everyone get a $2 for discount on wednesday


# age = int(input ("enter yor age "))
# day = input("enter the day ")
# price= 0
# price = 12 if age >=18 else 8 

# if day== "wednesday":
#     price= price-2

# print(price)


#3- grade calculator 
#Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

# score = int(input("enter the score "))
# if score >=101:
#     print("verify your score ")
#     exit()

# if score >90 :
#     print("A")
# elif score >=80:
#     print("B")
# elif score >=70:
#     print("C")
# elif  score >=60:
#     print("D")
# else :
#     print("F")


#4. Fruit Ripeness Checker
#Problem: Determine if a fruit is ripe, overripe, or unripe based on its color.
#  (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe


# fruit = "banana"
# color = input("enter the color ")

# if color ==  "green":
#     print("unripe ")
# elif color == "yellow":
#     print("ripe")
# elif color == "brown ":
#     print("overripe")


# 5. Weather Activity Suggestion
#Problem: Suggest an activity based on the weather 
# (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

# weather = input("Enter the weather: ").strip()  # strip() removes extra spaces
# if weather == "sunny":
#     activity = "go for a walk"
# elif weather == "rainy":
#     activity = "read a book"
# elif weather == "snowy":
#     activity = "build a snowman"
# else:
#     activity = "stay indoors"  # Optional: for unexpected inputs

# print(activity)


# #6. Transportation Mode Selection
# #Problem: Choose a mode of transportation based on the distance 
# # (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

# distance = int (input("eneter the distance "))

# if distance <3:
#     transport = "walk"
# elif distance <=15:
#     transport = "bike "
# else :
#     transport = "car "

# print(transport )


#7. Coffee Customization
#Problem: Customize a coffee order: 
# "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

# order_size= input("enetr the size ")
# extra_shot = bool(input("enter the extra shot"))

# if extra_shot== True:
#     coffee= order_size +  "extra shot of espresso"
# else :
#     coffee = order_size + "coffee"
# print("order:", coffee)

#8. Password Strength Checker
#Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).


# char = (input("enter the character "))

# if len(char) <6:
#     strength = "weak"
# elif len(char)<=10:
#     strength = "medium"
# else:
#     strength = "strong "

# print("password strength is :", strength)

#9. Leap Year Checker
#Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

# year = int (input ("enter the year "))
# if (year %400 ==0) or (year %4==0 and year %100 != 0 ):
#     print(year ,"year is a leap year")
# else:
#     print(year , "is not a leap year ") 


#10. Pet Food Recommendation
#Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).