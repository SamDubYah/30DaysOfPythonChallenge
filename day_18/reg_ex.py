#! /usr/bin/env python3

import re 


# ### Exercises: Level 1
#  1. What is the most frequent word in the following paragraph?
def get_wordcount(sentence):
    repattern = r'[A-Za-z]*[^\W]' #All words followed by either non word
    wordset = set(re.findall(repattern, sentence, re.I)) #Define as set to avoid duplicate items

    word_count_list = [] #

    for i in wordset:
        word_tup = (len(re.findall(i + '\W', sentence)), i) #Tupe of (count, word) where count is # of times word occured [ regex = word followed by non-word char (' ', '.')]
        word_count_list.append(word_tup) #Append tuple to list of tuple word coutns

    return sorted(word_count_list, reverse=True) #Return sorted list in Ascending order

paragraph = """I love teaching. If you do not love teaching what else can you love. 
            I love Python if you do not love something which can give you all the 
            capabilities to develop an application what else can you love."""

print(*get_wordcount(paragraph), sep='\n')

# ```sh
#     [
#     (6, 'love'),
#     (5, 'you'),
#     (3, 'can'),
#     (2, 'what'),
#     (2, 'teaching'),
#     (2, 'not'),
#     (2, 'else'),
#     (2, 'do'),
#     (2, 'I'),
#     (1, 'which'),
#     (1, 'to'),
#     (1, 'the'),
#     (1, 'something'),
#     (1, 'if'),
#     (1, 'give'),
#     (1, 'develop'),
#     (1, 'capabilities'),
#     (1, 'application'),
#     (1, 'an'),
#     (1, 'all'),
#     (1, 'Python'),
#     (1, 'If')
#     ]
# ```

# 2. The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
paragraph = """The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 
            0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles."""

def extract_numbers(text):  
    repattern = r'-?\d+'
    return [int(i) for i in re.findall(repattern, text)] #Return list of digits found in string as INTs


points = sorted(extract_numbers(paragraph))

distance = points[-1] - points[0]

print(f'{points[-1]} - {points[0]} = {distance}')


# ### Exercises: Level 2

# 1. Write a pattern which identifies if a string is a valid python variable

def is_valid_variable(text): 
    repattern = r'^[A-Za-z|_][A-Za-z0-9_]*$' #Verify text startes with A-Za-z or '_' and is followed by alpha numberic chars + '_' to end of string
    if re.match(repattern,text) != None:
        #print("True")
        return True
    else:
        #print("False")
        return False


print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name'))# False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname')) # True



# ### Exercises: Level 3

# 1. Clean the following text. After cleaning, count three most frequent words in the string.


sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

repattern = r'[^A-Za-z0-9\.\?\s]{1}' # Math all non Alpha-numeric Characters, '.', '?', spaces

print(*get_wordcount(re.sub(repattern,'',sentence)), sep='\n') #pass cleaned text to previously defined word_count function

