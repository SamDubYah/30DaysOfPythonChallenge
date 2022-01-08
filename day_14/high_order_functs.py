#! /usr/bin/env python3
from functools import reduce
import countries as countries_full
from countries_data import countries_data as cdata
from collections import Counter

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exercises: Level 1

#     Explain the difference between map, filter, and reduce.
# Map: return the iteration of a list through a function - single variable provided
# Filter: returns the true results of an interation of a list througha  function
# Reduce: returns the iteration of a list through a function - 2 variables provided


#     Explain the difference between higher order function, closure and decorator
# High Order Function: A function that either accepts a function as an argument or returns one
# Closure: 
# Decorator: 


#     Define a call function before map, filter or reduce, see examples.
def square(x):
    return x ** 2

print(list(map(square, numbers)))
print(list(map(lambda x : x**2, numbers)))

#     Use for loop to print each country in the countries list.
for ele in countries:
    print(ele, end=' ')

#     Use for to print each name in the names list.
for ele in names:
    print(ele, end=' ')

#     Use for to print each number in the numbers list.
for ele in numbers:
    print(ele, end=' ')

print()

# Exercises: Level 2

#     Use map to create a new list by changing each country to uppercase in the countries list
country_Upper = map(lambda x : x.upper(), countries)
print(list(country_Upper))

#     Use map to create a new list by changing each number to its square in the numbers list
numbers_squared = map(lambda x : x **2, numbers)
print(list(numbers_squared))

#     Use map to change each name to uppercase in the names list
names_Upper = map(lambda x : x.upper(), names)
print(list(names))

#     Use filter to filter out countries containing 'land'.
def contains_land(country):
    if 'land' in country.lower():
        return True
    else:
        return False

#land_countries = filter(contains_land, countries)
land_countries = filter(lambda x : True if 'land' in x.lower() else False, countries)
print(list(land_countries))

#     Use filter to filter out countries having exactly six characters.
def six_chars(string):
    if len(string) == 6:
        return True
    else:
        return False

#six_char_countries = filter(lambda x : True if len(x) == 6 else False, countries)
six_char_countries = filter(six_chars,countries)
print(list(six_char_countries))

#     Use filter to filter out countries containing six letters and more in the country list.
def six_or_more(string):
    if len(string) >= 6:
        return True
    else:
        return False

six_or_more_countries = filter(six_or_more, countries)
print(list(six_or_more_countries))

#     Use filter to filter out countries starting with an 'E'
def start_with_E(string):
    if string[0] == 'E':
        return True
    else:
        return False

start_with_E_countries = filter(start_with_E, countries)
print(list(start_with_E_countries))

#     Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
summation_of_square = reduce(lambda x,y: x+y, map(square,numbers))

print(summation_of_square)

#     Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(lst):
    return filter(lambda x : True if (type(x) == str) else False, lst)

combined_list = numbers + countries + names
only_string = get_string_lists(combined_list)

print(list(only_string))

#     Use reduce to sum all the numbers in the numbers list.
numb_sum = reduce(lambda x,y : x+y, numbers)

print(numb_sum)

#     Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
concat_countries = reduce(lambda x,y : x+', '+y, countries)

print(concat_countries, "are all European Countires")

#     Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
# Compares if two string share 2 or more characters

# Compares two strings to see if they are similar
def string_compare(str1, str2, sim_index):
    # 1. take string 1, and break into list of N characters (i.e N=2 'Eval' = ['Ev', 'va', 'al'])
    # 2. For each chunk in str_lst see if in str2
    #   a. check if chunk is less than sim_index
    # 3. If found return true else false

    #print(f"Comparing: {str1} and {str2} with a similarity of {sim_index} characters") # Debug string for compares
    str_lst = [str1[i:sim_index] for i in range(len(str1))] # Building the list from str1 as needed in step 1

    for ele in str_lst:
        if len(ele) < sim_index: #Check if element is less than similarity index (Should only ever be last element)
            break
        elif ele in str2:
            return True
        else:
            continue #Continues forloop if ele not in str2
    return False #Returns false if no match found


def categorize_countries(lst):
    # 1. Define the similarity index for how many characters to compare
    # 2. Compare each country against all other countries until either a match is found or all countries have been checked
    # 3. Return the list of results with atleast 1 comparison of sim_index
    returned_List = []
    sim_index = 2 # Number of characters to compare

    for i in range(0,len(lst)):
        for j in range(i + 1, len(lst)): #Start at 1 ele after i
            if string_compare(lst[i], lst[j], sim_index):
                returned_List.append(lst[i])
                break # Break out For j loop if match has been found

    return returned_List
    
cat_countries = categorize_countries(countries_full.countries)

print("The following Counties contain a match of 2 characters: ", ", ".join(cat_countries))

#     Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def country_First_Char(lst):
    # 1. Iterate through list of countries
    # 2. Check if first country letter is in dictionary
    #   a. If true: add 1 to count, else: add to dictionary and set value to 1
    # 3. return dictionary of letter counts

    letter_Count = {}

    for c in lst:
        if c[0].upper() in letter_Count.keys():
            letter_Count[c[0]] += 1
        else:
            letter_Count[c[0]] = 1
    
    return letter_Count

print(country_First_Char(countries_full.countries))

#     Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten_countries():
    return countries_full.countries[:10]

print(get_first_ten_countries())

#     Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries():
    return countries_full.countries[-10:]

print(get_last_ten_countries())


# Exercises: Level 3

#     Use the countries_data.py (master/data/countries-data.py) file and follow the tasks below:
#         Sort countries by name, by capital, by population
#         Sort out the ten most spoken languages by location.
#         Sort out the ten most populated countries.

def sort_by_name():
    return sorted([country['name'] for country in cdata])

def sort_by_capital():
    return sorted([(country['name'],country['capital']) for country in cdata], key = lambda x: x[1],reverse=True)

def sort_by_population():
    return sorted([(country['name'], country['population']) for country in cdata], key = lambda x: x[1],reverse=True)

def ten_most_spoken():
    languages_dict = {}

    for country in cdata:
        for language in country['languages']:
            if language in languages_dict.keys():
                languages_dict[language] += 1
            else:
                languages_dict[language] = 1

    return sorted(languages_dict.items(), key = lambda x: x[1],reverse=True)[:10]

def ten_most_populated():
    return sort_by_population()[:10]

print(sort_by_name())
print(sort_by_capital())
print(sort_by_population())

print(ten_most_spoken())
print(ten_most_populated())