#! /usr/bin/env python3
from random import randint
import string

# ### Exercises: Level 1

# 1. Writ a function which generates a six digit/character random_user_id.
def random_user_id():
    userid =''
    alpha_num = string.ascii_letters + string.digits
    
    for i in range(0, 7, 1):
        rand_index = randint(0, len(alpha_num)-1)
        userid += alpha_num[rand_index]

    return userid

print(random_user_id())



# 2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    user_count = int(input('Number of Users: '))
    id_size = int(input('Length of userid: '))
    alpha_num = string.ascii_letters + string.digits # Alphanumeric string for generation
    user_ids = [] # Empty list of user ids to be populated
    
    for user in range(0,user_count,1): 
        new_id = ''
        for i in range(0, id_size, 1):
            rand_index = randint(0, len(alpha_num)-1)
            new_id += alpha_num[rand_index]
        user_ids.append(new_id)
    
    return user_ids
        

# print(user_id_gen_by_user()) # user input: 5 5
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf
   
# print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr


# 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)

    return red, green, blue


print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form


# ### Exercises: Level 2

# 1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hex_colors(num_to_gen):
    hex_colors = []

    for hex_color in range(0,num_to_gen,1):
        new_color = ''
        for i in range(0, 6, 1):
            new_color += string.hexdigits[randint(0, 16)]
        
        hex_colors.append('#'+new_color)

    return hex_colors

print(list_of_hex_colors(6))

# 1. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(num_to_gen):
    rgb_colors = []

    for rgb_color in range(0, num_to_gen,1):
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)
        rgb = red, green, blue

        rgb_colors.append('rgb' + str(rgb))
    return rgb_colors

print(list_of_rgb_colors(3))

# 1. Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(ctype, num_to_gen):
    if ctype == 'hexa':
        return list_of_hex_colors(num_to_gen)
    elif ctype == 'rgb':
        return list_of_rgb_colors(num_to_gen)
    else:
        print('Invalid Color Type [hexa, rgb]')

print(generate_colors('hexa', 3)) # ['#a3e12f','#03ed55','#eb3d2b'] 
print(generate_colors('hexa', 1)) # ['#b334ef']
print(generate_colors('rgb', 3))  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
print(generate_colors('rgb', 1))  # ['rgb(33,79, 176)']



# ### Exercises: Level 3

# 1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(lst):
    shuffled_lst = []
    for i in range(0, len(lst)):
        shuffled_lst.insert(randint(0, len(lst)), lst[i])
    
    return shuffled_lst
   
list_to_shuffle = ['sam', 'ty', 'gaming', 'age', 'lame', 'somethingmore']
print(shuffle_list(list_to_shuffle))

# 1. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def array_of_seven():
    numbers = set({})
    while(len(numbers) < 8):
        numbers.add(randint(0, 9))
    return numbers

print(array_of_seven())