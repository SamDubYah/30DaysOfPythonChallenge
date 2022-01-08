#! /usr/bin/env python3

# 1. Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
pos_nums = [i for i in numbers if i >= 0]
print(pos_nums)


# 2. Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flattened = [number for row in list_of_lists for number in row]

print(flattened)

#    output
#    [1, 2, 3, 4, 5, 6, 7, 8, 9]


# 3. Using list comprehension create the following list of tuples:
#    ```py
#    [(0, 1, 0, 0, 0, 0, 0),
#    (1, 1, 1, 1, 1, 1, 1),
#    (2, 1, 2, 4, 8, 16, 32),
#    (3, 1, 3, 9, 27, 81, 243),
#    (4, 1, 4, 16, 64, 256, 1024),
#    (5, 1, 5, 25, 125, 625, 3125),
#    (6, 1, 6, 36, 216, 1296, 7776),
#    (7, 1, 7, 49, 343, 2401, 16807),
#    (8, 1, 8, 64, 512, 4096, 32768),
#    (9, 1, 9, 81, 729, 6561, 59049),
#    (10, 1, 10, 100, 1000, 10000, 100000)]
#    ```
      
power_list = [tuple([row] + [row ** column for column in range(6)]) for row in range(11)]

print('\n '.join([str(i) for i in power_list]))

# 4. Flatten the following list to a new list:
#    ```py
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#    output:
#    [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
#    ```

country_list = [[i[0].upper() if j==0 else i[0][:3].upper() if j==1 else i[1].upper() for i in country for j in range(3)] for country in countries]      

print(country_list)


# 5. Change the following list to a list of dictionaries:
#    ```py
#    countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#    output:
#    [{'country': 'FINLAND', 'city': 'HELSINKI'},
#    {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
#    {'country': 'NORWAY', 'city': 'OSLO'}]
#    ```

country_dict = [{'country': tup[0].upper(), 'city': tup[1].upper()} for lst in countries for tup in lst]

print(country_dict)

# 6. Change the following list of lists to a list of concatenated strings:
#    ```py
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
#    output
#    ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
#    ```
first_last = [' '.join(name_tup) for name_lst in names for name_tup in name_lst]

print(first_last)

# 7. Write a lambda function which can solve a slope or y-intercept of linear functions.

slope_intercept = lambda x1, y1, x2, y2, solve: (y2 - y1) / (x2 - x1) if solve.lower() == 'slope' else y2 - (slope_intercept(x1,y1,x2,y2,'slope') * x2) if solve.lower() == 'intercept' else 'Bad Input!'

print(slope_intercept(10,20,1,0,'slope'))
print(slope_intercept(10,20,0,0,'intercept'))