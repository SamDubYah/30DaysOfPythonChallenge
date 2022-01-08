#!/usr/bin/env python3
from math import pi

#Exercise 1
# 1
# 2
print("Day 2: 30 days of python programming")
# 3
first_name = "samuel"
# 4
last_name = "warner"
# 5
full_name = "Samuel Warner"
# 6
country = "United States"
# 7
city = "Colorado Springs"
# 8
age = 25
# 9
year = 2021
# 10
is_married = False
# 11
is_true = True
# 12
is_light_on = False #Always... never work in the light
# 13
variable1, string_variable, some_other_variable = 10, "This is a string", ['not', 'sure', 'what', 'to', 'assign']

#Exercise 2
# 1
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(variable1))
print(type(string_variable))
print(type(some_other_variable))

# 2
print(len(first_name))
print(len(last_name))

# 3
print("First Name Length: ", first_name)
print("Last Name Length: ", last_name)
if(len(first_name) > len(last_name)):
    print ("First name is longer...", len(first_name))
elif(len(first_name) < len(last_name)):
    print ("Last name is longer... ", len(last_name))
else:
    print("Both First Name {",len(first_name),"} and Last Name{", len(last_name),"} Are equal")

# 4
num_one = 5
num_two = 4
# # i 
print("Addition: ",num_one + num_two)
# # ii
print("Subtraction: ",num_one - num_two)
# # iii
print("Multiplication: ",num_one * num_two)
# # iv
print("Division: ",num_one / num_two)
# # v
print("Modulus: ", num_one % num_two)
# # vi
print("Exponential: ", num_one ** num_two)
# # vii
print("Floor: ",num_one // num_two)
1
# 5
radius = 30 #meters
# # i
area_of_circle = (pi * (radius**2))
print("Area of Circle: ", area_of_circle)
# # ii
circum_of_circle = (2 * (pi * radius))
print("Circumference of Circle: ", circum_of_circle)
# # iii
radius = input("Enter a new radius")
print("New area = ", (pi * (int(radius) ** 2)))

# 6
first_name = input("First Name: ")
last_name = input("Last Name: ")
country = input("Country: ")
age = input ("Age: ")

# 7
help('keywords')
