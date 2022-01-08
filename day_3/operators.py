#! /usr/bin/env python3
import math
from sympy import symbols, Eq, solve

# 1
age = 25
# 2
height = 75.00
# 3
complex_num = 4j + 8

# 4
def area_of_triangle():
    # User input to define base/height
    height = int(input("Enter Triangle Height: "))
    base = int(input("Enter Triangle Base: "))

    # Calculate the area
    area = .5 * base * height

    print(area)

area_of_triangle()
# 5
def circum_of_triangle():
    # User input to define sides of traingle
    side_a = int(input("Enter side A: "))
    side_b = int(input("Enter side B: "))
    side_c = int(input("Enter side C: "))

    perimeter = side_a + side_b + side_c

    print("Perimeter of Triangle: ",perimeter)

circum_of_triangle()
# 6
rect_length = int(input("Enter Rectangle length: "))
rect_width = int(input("Enter Rectangle Width: "))

rect_perimeter = 2 * (rect_length + rect_width)
rect_area = rect_length * rect_width

print("Peremiter of Rectangle: ",rect_perimeter)
print("Area of Rectangle: ",rect_area)

# 7
circ_radius = int(input("Radius of Circle: "))

circ_area = math.pi * (circ_radius**2) 
circ_circumference = (2 * math.pi * circ_radius)

# 8
#X,Y = (0,0) - Intercept points for when x = 0 and y = 0
xy = [0,0]

y_intercept = 2*xy[0]- 2
x_intercept = (xy[1] + 2)/2

print("X intercept: ",x_intercept)
print("Y intercept: ",y_intercept)

print("Slope = 2")
# 9
point_one = [2,2]
point_two = [6,10]

slope = (point_two[0] - point_one[0]) / (point_two[1] - point_one[1])

#square root ((q1 - p1)**2 + (q2 - p2)**2)
euclidean =  math.dist(point_one, point_two)

print("Slope: ", slope)
print("Euclidean: ", euclidean)

# 10
#Slopes are 2 and 1/2

# 11
#y = x**2 + 6x + 9

def solv_Y():
    x = symbols('x')

    solution = solve((x**2) + (6*x) + 9)
    print("Solution is: ", solution)
solv_Y()

# 12
print(len("Python") != len("Dragon"))
print(len("Python") == len("Dragon"))
print(len("Python") <= len("Dragon"))
print(len("Python") > len("Dragon"))

# 13
print("on" in ("dragon" and "python"))

# 14
sentence = "i hope this course is not full of jargon"

if("jargon" in sentence):
    print ("jargon in sentence")


# 15
print("on" not in ("dragon" and "python"))

# 16
print(type(str(float(len("python")))))

# 17
user_num = int(input("Enter a number: "))
if((user_num % 2) == 0 ):
    print("Number is Even")
else:
    print("Number is Odd")

# 18
#is 7//3 == int(2.7)
print((7//3) == int(2.7))

# 19
#is type '10' == 10
print(type(10) == 10)

# 20
#is int(9.8) == 10
print(int(9.8) == 10)

# 21
#weekly pay
def calculate_pay():
    hours = int(input("Enter Hours Worked: "))
    pay = float(input("Enter Pay Rate: "))
    weekly = int(hours * pay)

    print("Your pay this week is: ",weekly)

# 22
def seconds_lived():
    year_alive = int(input("Enter your Age/Years alive: "))
    year_to_seconds = int(year_alive * 365 * 24 * 60 * 60)

    print("Seconds Alive: ", year_to_seconds)

# 23

# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

print("""
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125""")
    
    