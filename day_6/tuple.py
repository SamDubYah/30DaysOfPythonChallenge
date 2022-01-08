#!/usr/bin/env python3
import man_lists

# ## Exercises: Day 6

# ### Exercises: Level 1

# 1. Create an empty tuple
empty_tuple = ()
print('Empy Tupel: \t', empty_tuple)

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Jaz', 'Devon')
sisters = ('Karly',)
print('Siblings: \t', brothers, sisters)

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print('Siblings: \t', siblings)

# 4. How many siblings do you have?
print('Sibling count: \t', len(siblings))

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
# Cant modify the tuple
parents = ('Doug','Shelley')
family_members = parents + siblings
print('Family: \t', family_members)

# ### Exercises: Level 2

# 1. Unpack siblings and parents from family_members
father, mother, brother_one, brother_two, sister = family_members

# 1. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('mango', 'apple', 'pineapple')
vegetables = ('cucumber', 'lettuce', 'brocoli')
animal_products = ('meat', 'cooked meat', 'raw meat')

food_stuff_tp = fruits + vegetables + animal_products

print('Food Stuff: \t', food_stuff_tp)

# 1. Change the about food_stuff_tp  tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# 1. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print('Middle Item[s]: \t', man_lists.middleList(food_stuff_tp))

# 1. Slice out the first three items and the last three items from food_staff_lt list
print('Last Three: \t', food_stuff_lt[-3:])

# 1. Delete the food_staff_tp tuple completely
del food_stuff_tp

# 1. Check if an item exists in  tuple:

# - Check if 'Estonia' is a nordic country
# - Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia Exists: \t', 'Estonia' in nordic_countries)
print('Iceland Exists: \t', 'Iceland' in nordic_countries)