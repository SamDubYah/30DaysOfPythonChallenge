#!/usr/bin/env python3
import sys
from math import dist

#Exercise 1

# Question 1
print(sys.version_info)

# Question 2
print(3+4) #Addition
print(3-4) #Subtraction
print(3*4) #Multiplication
print(3/4) #Division
print(3%4) #Modulus Division
print(3//4)#Floor Division
print(3**4)#Exponential Multiplication

# Question 3
print("Samuel")
print("Warner")
print("USA")
print("I am enjoying 30 days of python")

# Question 4
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type("Samuel"))
print(type("Warner"))
print(type("United States"))

#Exercise 3
# Question 1
print(type(10))     #Int
print(type(9.8))    #Float
print(type(4-4j))   #Complex
print(type(['Asabeneh', 'Python', 'Finland']))#List
print(type("Samuel"))#String
print(type(True))   #boolean
print(type(('something','else','something_else'))) #tuple
print(type({'Name':'James','Car':'Nissan Shitbox','Age':30})) #dict
print(type({1,4,2,5,3})) #set
# Question 2
print("Distance with math func: ",dist((2,3),(10,8)))