#! /usr/bin/env python3
from countries import countries
from countries_data import countries_data
from collections import Counter

## 💻 Exercises: Day 10

### Exercises: Level 1

# 1. Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(0,11):
    print(i, end=' ')
print()

count = 0
while count < 11:
    print(count, end=' ')
    count += 1
print()

# 2. Iterate 10 to 0 using for loop, do the same using while loop.

for i in range(10,-1,-1):
    print(i, end=' ')
print()

count = 10
while count > -1:
    print(count, end=' ')
    count -= 1
print()

# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:

#    ```py
#      #
#      ##
#      ###
#      ####
#      #####
#      ######
#      #######
#    ```
for i in range(1,8):
    print('#' * i)

#alternate method - this method sucks
for i in range(1,8):
    for j in range(0,i):
        print('#', end='')
    print()

# 4. Use nested loops to create the following:

#    ```sh
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    ```
for i in range(1,9):
    for j in range(1,9):
        print('#', end=' ')
    print()

# 5. Print the following pattern:

#    ```sh
#    0 x 0 = 0
#    1 x 1 = 1
#    2 x 2 = 4
#    3 x 3 = 9
#    4 x 4 = 16
#    5 x 5 = 25
#    6 x 6 = 36
#    7 x 7 = 49
#    8 x 8 = 64
#    9 x 9 = 81
#    10 x 10 = 100
#    ```

for i in range(0,11):
    print(f'{i} x {i} = {i*i}')

# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
lst = ['Python', 'Numpy','Pandas','Django', 'Flask']

for i in lst:
    print(i)

# 7. Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(0,101,2):
    if i == 0: # 0 Is not mathmatically even
        pass
    else:
        print(i)

# 8. Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(0,100,2):
    print(i+1)

# ### Exercises: Level 2
    
# 1.  Use for loop to iterate from 0 to 100 and print the sum of all numbers.

#    ```sh
#    The sum of all numbers is 5050.
#    ```

loop_sum = 0
for i in range(0,101):
    loop_sum += i

print(loop_sum)

# 2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

#     ```sh
#     The sum of all evens is 2550. And the sum of all odds is 2500.
#     ```

sum_even = 0
sum_odd = 0

for i in range(0,101):
    if i%2 == 0:
        sum_even += i
    elif i%2 != 0:
        sum_odd += i
    
print(f'The sum of all the evens is {sum_even}, the sum of all odds is {sum_odd}')    





# ### Exercises: Level 3

# 1. Go to the data folder and use the [countries.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) file. Loop through the countries and extract all the countries containing the word _land_.

land_countries = []

for i in countries:
    if 'land' in i:
        land_countries.append(i)

print(land_countries)

# 2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_reverse = []

for i in fruits:
    fruits_reverse.insert(0, i)

print (fruits_reverse)

# 3. Go to the data folder and use the [countries_data.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file. 
#    1. What are the total number of languages in the data
print('\n\n')
languages_set = set({})

for country in countries_data:
    for language in country['languages']:
        languages_set.add(language)
    
print(f'There are {len(languages_set)} unique languages in countries_data')

#    2. Find the ten most spoken languages from the data
print('\n\n')

languages_dict = {}

for country in countries_data:
    for language in country['languages']:
        if language in languages_dict.keys():
            languages_dict[language] += 1
        else:
            languages_dict[language] = 1

lang_high10 = Counter(languages_dict).most_common(10)

print(lang_high10, '\n\n')

#    3. Find the 10 most populated countries in the world

country_pop = {}

for country in countries_data:
    name = country['name']
    population = country['population']
    country_pop[name] = population

country_pop10 = Counter(country_pop).most_common(10)

print(country_pop10)