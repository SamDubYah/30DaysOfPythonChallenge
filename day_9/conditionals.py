#! /usr/bin/env python3

import man_lists

# ### Exercises: Level 1

# 1.  Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
#     ```sh
#     Enter your age: 30
#     You are old enough to learn to drive.
#     Output:
#     Enter your age: 15
#     You need 3 more years to learn to drive.
#     ```

age = int(input('Enter your age: '))

if age > 18:
    print('You are old enough to learn to drive')

elif age < 18:
    print('You must {} more years to learn to drive'.format(21 - age)) 

else:
    print('We dont take to kindly to your kind \'round these parts')


# 2.  Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
#     ```sh
#     Enter your age: 30
#     You are 5 years older than me.
#     ```
my_age = 45
your_age = int(input('Enter your age: '))

age_diff = my_age - your_age

#You are older
if age_diff < 0:
    if age_diff == -1:
        print('You are 1 year older')
    else:
        print(f'You are {age_diff} years older')
elif age_diff > 0:
    if age_diff == 1:
        print('I am 1 year older')
    else:
        print(f'I am {age_diff} years older')
else:
    print('I see you and what you did')


# 3.  Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
# ```sh
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
# ```
num_a = int(input('Enter a Number: '))
num_b = int(input('Enter b Number: '))

if num_a > num_b:
    print(f'{num_a} is greater than {num_b}')
elif num_a < num_b:
    print(f'{num_a} is less than {num_b}')
else:
    print(f'{num_a} is equal to {num_b}')


#     ### Exercises: Level 2

#    1. Write a code which gives grade to students according to theirs scores:
   
#         ```sh
#         80-100, A
#         70-89, B
#         60-69, C
#         50-59, D
#         0-49, F
#         ```

def letter_grade(num_grade):
    if 80 <= num_grade <= 100:
        return 'A'
    elif 70 <= num_grade <= 89:
        return 'B'
    elif 60 <= num_grade <= 69:
        return 'C'
    elif 50 <= num_grade <= 59:
        return 'D'
    elif 0 <=num_grade <= 49:
        return 'F'
    else:
        print('you fucked up')
        exit('1')

print('Grade: \t', letter_grade(25))
# 1. Check if the season is Autumn, Winter, Spring or Summer. If the user input is:
#     September, October or November, the season is Autumn.
#     December, January or February, the season is Winter.
#     March, April or May, the season is Spring
#     June, July or August, the season is Summer

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

print('Season: ', get_season('DEcEmber'))

# 2.  The following list contains some fruits:
#     ```sh
#     fruits = ['banana', 'orange', 'mango', 'lemon']
#     ```
#     If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list') 

#     ### Exercises: Level 3

fruits = ['banana', 'orange', 'mango', 'lemon']

new_fruit = str(input('Enter a Fruit: '))

if new_fruit.lower() in fruits:
    print('That Fruit already exists')
else:
    fruits.append(new_fruit)
    print('New Fruit Added', fruits)


#    1. Here we have a person dictionary. Feel free to modify it!
   

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}


#      * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person.keys():
    print('Middle Skill: \t', man_lists.middleList(person['skills'])) #Calling previously made middle definition from man_lists(Manipulate Lists)
else:
    print('No skills for this person')

#      * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person.keys():
    if 'Python' in person['skills']:
        print('Python Found')
    else:
        print('No Python')
else:
    print('No Skills')

#      * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

if ['JavaScript','React'] in person['skills']:
     print('He is a front end Developer')
elif ['Node', 'Python', 'MongoDB'] in person['skills']:
    print('He is a backend Developer')
elif ['JavaScript', 'React', 'Node','Python', 'MongoDB' ]:
    print('He is a fullstack Developer')
else:
    print('unknown title')

#      * If the person is married and if he lives in Finland, print the information in the following format:
if person['is_marred'] == True and person['country'] == 'Finland': 
    print ('{} {} lives in {}. He is Married'.format(person['first_name'],person['last_name'], person['country']))

# ```py
#     Asabeneh Yetayeh lives in Finland. He is married.
# ```


