#!/usr/bin/env python3 

import cmath
import math
import countries_data as cdata
from collections import Counter

### Exercises: Level 1

# 1. Declare a function _add_two_numbers_. It takes two parameters and it returns a sum.
def sum_two(num1, num2):
    return num1 + num2

# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates _area_of_circle_.
def area_of_circle(radius):
    return radius ** 2

# 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def sum_any(*nums):
    total = 0
    for num in nums:
        if type(num) == int or type(num) == float:
            total += num
        else:
            print(f'{num} is of {type(num)} which is not valid for sum. Skipping')
    
    return total

print('Sum_All: \t', sum_any(0,33,4.5,'test',5.5,8.00003))  

# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, _convert_celsius_to-fahrenheit_.
def celsius_to_fahrenheit(celsius):
    if type(celsius) != int and type(celsius) != float:
        return f'{celsius} {type(celsius)} - provided value is invalid for converstion.'
    else:
        return (celsius * (9/5) + 32)

print(celsius_to_fahrenheit(100))

# 5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
### This was already done as part of another challenge, below is copy pasta from 
def get_season(month):
    if month.lower() in ('september', 'october', 'november'):
        return 'Autumn'
    elif month.lower() in ('december', 'january', 'february'):
        return 'Winter'
    elif month.lower() in ('march', 'april', 'may'):
        return 'Spring'
    elif month.lower() in ('june', 'july', 'august'):
        return 'Summer'
    else:
        print('you fucked up')
        exit('1')


# 6. Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(linearEq):
    #Function steps to success
    # 1. Verify recived variable is of type string (Expecting either y = mx + b or mx + b)
    # 2. Repalce 'x' with '*1j' to convert to complex number
    # 3. Remove 'y' && '=' as they arent needed
    # 4. Return the evaluted formula's Imaginary number

    if type(linearEq) != str: # Ensure recieved format is string. 
        print('Invalid type recieved. Expecting Format of ([y = ] mx + b)')
        return 
    else:
        eq_formatted = linearEq.replace('x', '*1j') # replace 'x' with '*1j' to format to complex
        eq_formatted = eq_formatted.replace('y','') # replace 'y' with nothing
        eq_formatted = eq_formatted.replace('=', '')# replace '=' with nothing
        eq_formatted = eq_formatted.strip() # Strip leading/trailing whitespace to clean formatting

        return(eval(eq_formatted).imag) # Return evalutated formual's imaginary ('**1j') number
     
    
print('Slope: \t', calculate_slope('y = 5/4x + 10'))

# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, _solve_quadratic_eqn_.
def solve_quadratic(a, b, c):
    # Solution = (-b ± √ (b)**2 - 4*a*c) / (2*a)
    # ± can be handled by solving twice
    solution1 = (-b + cmath.sqrt((b**2) - (4*a*c))) / (2*a)
    solution2 = (-b - cmath.sqrt((b**2) - (4*a*c))) / (2*a)

    return solution1.real, solution2.real

solution = solve_quadratic(1, 5, 6)
print('Solution 1: \t{0:.2f}\nSolution 2: \t{1:.2f}'.format(solution[0],solution[1]))

# 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for ele in lst:
        print(ele, end=' ')
    print()

print_list([1, 2,3,4,5,7,2,34])

# 9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(lst):
    rev_list = []
    for ele in lst:
        rev_list.insert(0, ele)
    return rev_list


print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))
# ["C", "B", "A"]


# 10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lst):
    cap_list = []

    if type(lst) != list:
        return 0

    for ele in lst:
        cap_list.append(ele.capitalize())
    return cap_list


print(capitalize_list_items(['sam', 'test', 'something']))


# 11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(lst, item):
    app_list = lst
    app_list.append(item)
    return app_list

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))      #[2, 3, 7, 9, 5]

# 12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(lst, item):
    rem_list = lst
    rem_list.remove(item)
    
    return rem_list
    

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]


# 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(num):
    sum_all = 0
    for num in range(0, num + 1, 1):
        sum_all += num
    return sum_all

print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050


# 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_odds(number):
    sum_odd = 0
    for num in range(1, number +1, 2):
        sum_odd += num
    return sum_odd

print(sum_odds(100))

# 15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_evens(number):
    sum_even = 0
    for num in range(0, number +1, 2):
        sum_even += num
    return sum_even

print(sum_evens(100))


# ### Exercises: Level 2

# 1.  Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(number):
    even_count = 0
    odd_count = 0

    for num in range(0 , number + 1, 1):
        if num % 2 == 0:
            even_count += 1
        elif num % 2 != 0:
            odd_count += 1
        else:
            print('You fucked up!')
            exit(0)
    
    print('The number of odds are: \t', odd_count)
    print('The number of evens are: \t', even_count)

    
print(evens_and_odds(100))
# The number of odds are 50.
# The number of evens are 51.


# 1. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(whole_num):
    factor = 1
    if type(whole_num) != int:
        print('Expecting Integer')
        return 0
    else:
        for num in range(1, whole_num+1, 1):
            factor *= num
    
    return factor

print(factorial(5))

# 1. Call your function _is_empty_, it takes a parameter and it checks if it is empty or not
def is_empty(param):
    if type(param) == int:
        if param == 0:
            return 'Not empty but storing \'0\''
        else:
            return f'Not empty, storying {param}'
    elif len(param) == 0:
        return 'parameter is empty'
    else:
        return 'parameter is not empty'

test=[]

print(is_empty(test))

# 1. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
num_list = [1, 2, 5, 7, 7, 7, 8, 10, 34]

def calculate_mean(num_list):
    # sum of elements / number of elements
    mean = sum(num_list) / len(num_list)
    return mean

print('Mean: {:.2f}'.format(calculate_mean(num_list)))

def calculate_median(num_list):
    # Middle point[s] of the list
    if len(num_list) % 2 == 0:
        # Returning 2 numbers for both mid points
        median = []

        med1 = num_list[int(len(num_list) / 2)-1] 
        med2 = num_list[int(len(num_list)/2)]

        median += med1, med2
        
        return median
    else:
        # Returning just the 1 midpoint
        median = num_list[int(len(num_list)/2)]
        return median 

print('Median: {}'.format(calculate_median(num_list)))

def calculate_mode(num_list):
    mode_dict = {}

    # iterate through items, assinging occurance for each value
    for num in num_list:
        if not num in mode_dict:
            mode_dict[num] = 1
        else:
            mode_dict[num] += 1
    
    # get max value and max key
    max_value = max(mode_dict.values())
    max_key = [k for k, v in mode_dict.items() if v == max_value]
    
    # return both value and key
    return (max_value, max_key)

print('Mode: {}'.format(calculate_mode(num_list)))

def calculate_range(num_list):
    return max(num_list) - min(num_list)

print('Range: {}'.format(calculate_range(num_list)))

def calculate_variance(num_list):
    mean = calculate_mean(num_list)
    var = 0
    for num in num_list:
        var += (num - mean) ** 2
    
    var = var / (len(num_list))
    return var

print('Variance: {}'.format(calculate_variance(num_list)))

def calculate_std(num_list):
    # Standard deviation = sqrt((abs(sum(num - mean ** 2))/9))
    mean = calculate_mean(num_list)
    sum_of_square = 0
    for num in num_list:
        sum_of_square += abs(num - mean) ** 2
    
    print(sum_of_square)

    std_deviate = math.sqrt((sum_of_square)/9)
    return std_deviate

print('STD Deviation: {}'.format(calculate_std(num_list)))

# ### Exercises: Level 3

# 1. Write a function called is_prime, which checks if a number is prime.
def is_prime(num):
    if num > 1: 
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return False
        else:
            return True 
    else:
        return False

print(is_prime(11))
        
# 1. Write a functions which checks if all items are unique in the list.
def is_unique(lst):
    for i in lst:
        if lst.count(i) > 1:
            return False
    else:
        return True

test_lst = ['a', 'b', 'd']
# 1. Write a function which checks if all the items of the list are of the same data type.
def same_type(lst):
    
    for i in range(0, len(lst)):
        print(lst[i])
        for j in range(i+1,len(lst)):
            if type(lst[i]) != type(lst[j]):
                return False 
    else:
        return True
        
print(same_type(test_lst))

# 1. Write a function which check if provided variable is a valid python variable
def is_valid(var):
    return var.isidentifier()

print(is_valid('var'))

# 1. Go to the data folder and access the countries-data.py file.

# - Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order

languages_dict = {}

def most_spoken_languages(countries_data):
    
    for country in countries_data:
        for language in country['languages']:
            if language in languages_dict.keys():
                languages_dict[language] += 1
            else:
                languages_dict[language] = 1

    lang_high10 = Counter(languages_dict).most_common(10)

    return lang_high10


print(most_spoken_languages(cdata.countries_data))

# - Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.

country_pop = {}

def most_populated_countries(countries_data):
    for country in countries_data:
        name = country['name']
        population = country['population']
        country_pop[name] = population

    country_pop10 = Counter(country_pop).most_common(10)

    return country_pop10

print(most_populated_countries(cdata.countries_data))
