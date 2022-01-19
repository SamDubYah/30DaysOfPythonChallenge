#! /usr/bin/env python3
import re
import json
import csv
import math
import sys
import string


def read_file(filename):
    """Trys to read file then returns data"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = file.read()
        return data
    except IOError:
        print("Error opening or reading file: ", filename)
        sys.exit()


# ### Exercises: Level 1

# 1. Write a function which count number of lines and number of words in a text. All the files are in the data the folder:
#    a) Read obama_speech.txt file and count number of lines and words
#    b) Read michelle_obama_speech.txt file and count number of lines and words
#    c) Read donald_speech.txt file and count number of lines and words
#    d) Read melina_trump_speech.txt file and count number of lines and words

def count_lines(text):
    count = 0
    with open(text,'r') as f:
        for line in f.readlines():
            if not line.isspace():
                count +=1
    return count


def count_words(text):
    count = 0
    with open(text,'r') as f:
        for line in f.readlines():
            for word in re.findall('[A-Za-z]+', line):
                count += 1
    return count


print("## Exercise Leve 1\n")
print("Melina Trump speech line count: \t", count_lines("./melina_trump_speech.txt"))
print("Donald Trump speech line count: \t", count_lines("./donald_speech.txt"))
print("Barrack Obama speech line count: \t",count_lines("./obama_speech.txt"))
print("Michelle Obama speech line count: \t",count_lines("./michelle_obama_speech.txt"))

print("Melina Trump speech word count: \t", count_words("./melina_trump_speech.txt"))
print("Donald Trump speech word count: \t", count_words("./donald_speech.txt"))
print("Barrack Obama speech word count: \t",count_words("./obama_speech.txt"))
print("Michelle Obama speech word count: \t",count_words("./michelle_obama_speech.txt"))

# 2. Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages

#    ```py
#    # Your output should look like this
#    print(most_spoken_languages(filename='./data/countries_data.json', 10))
#    [(91, 'English'),
#    (45, 'French'),
#    (25, 'Arabic'),
#    (24, 'Spanish'),
#    (9, 'Russian'),
#    (9, 'Portuguese'),
#    (8, 'Dutch'),
#    (7, 'German'),
#    (5, 'Chinese'),
#    (4, 'Swahili'),
#    (4, 'Serbian')]

def most_spoken_languages(fname, topCount):
    lang_count = {}

    with open(fname, 'r') as f:
        jdata = json.load(f)
        for i in jdata:
            for lang in i['languages']:
                if lang in lang_count.keys():
                    lang_count[lang] += 1
                else:
                    lang_count[lang] = 1

    return sorted([(v,k) for k,v in lang_count.items()], reverse=True)[:topCount]

print(*most_spoken_languages("./countries_data.json", 10), sep="\n")
print()

#    # Your output should look like this
#    print(most_spoken_languages(filename='./data/countries_data.json', 3))
#    [(91, 'English'),
#    (45, 'French'),
#    (25, 'Arabic')]
#    ```
print(*most_spoken_languages('./countries_data.json', 3), sep="\n")


# 3. Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

#    ```py
#    # Your output should look like this
#    print(most_populated_countries(filename='./data/countries_data.json', 10))

#    [
#    {'country': 'China', 'population': 1377422166},
#    {'country': 'India', 'population': 1295210000},
#    {'country': 'United States of America', 'population': 323947000},
#    {'country': 'Indonesia', 'population': 258705000},
#    {'country': 'Brazil', 'population': 206135893},
#    {'country': 'Pakistan', 'population': 194125062},
#    {'country': 'Nigeria', 'population': 186988000},
#    {'country': 'Bangladesh', 'population': 161006790},
#    {'country': 'Russian Federation', 'population': 146599183},
#    {'country': 'Japan', 'population': 126960000}
#    ]

#    # Your output should look like this

#    print(most_populated_countries(filename='./data/countries_data.json', 3))
#    [
#    {'country': 'China', 'population': 1377422166},
#    {'country': 'India', 'population': 1295210000},
#    {'country': 'United States of America', 'population': 323947000}
#    ]
#    ```

def most_populated_countries(fname, topCount):
    country_pop = {}
    with open(fname, 'r') as f:
        jdata = json.load(f)
        for i in jdata:
            country_pop[i['name']] = i['population']
    
    return sorted(country_pop.items(), key = lambda x : x[1], reverse=True)[:topCount]

print(*most_populated_countries('./countries_data.json', 3), sep='\n')
print()
print(*most_populated_countries('./countries_data.json', 10), sep='\n')


# ### Exercises: Level 2

# 4. Extract all incoming email addresses as a list from the email_exchange_big.txt file.
def get_from_addresses(email_txtObj):
    data = email_txtObj.read() 
    emails = set([x for x in re.findall('([a-z\.]+@[a-z\.]+)', data) if 'localhost' not in x]) #Return list of emails excluding items containing 'localhost'
    return emails

with open('./email_exchange_big.txt', 'r') as f:
    print(get_from_addresses(f))

# 5. Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output

# ```py
#     # Your output should look like this
#     print(find_most_common_words('sample.txt', 10))
#     [(10, 'the'),
#     (8, 'be'),
#     (6, 'to'),
#     (6, 'of'),
#     (5, 'and'),
#     (4, 'a'),
#     (4, 'in'),
#     (3, 'that'),
#     (2, 'have'),
#     (2, 'I')]

#     # Your output should look like this
#     print(find_most_common_words('sample.txt', 5))

#     [(10, 'the'),
#     (8, 'be'),
#     (6, 'to'),
#     (6, 'of'),
#     (5, 'and')]
# ```


def find_most_common_words(word_lst, com_count=-1):
    """Returns the top 'com_count' number of words with thier freq in a tuple
    com_count default value return all items"""
    wc_dict = {}
    for i in word_lst:
        if i in wc_dict:
            wc_dict[i] = wc_dict[i] + 1
        else:
            wc_dict[i] = 1

    return sorted([(v, k) for k, v in wc_dict.items()],
                  reverse=True)[:com_count]


with open('./email_exchange_big.txt', 'r', encoding='utf-8') as f:
    print(find_most_common_words(f.read(), 10))

# 6. Use the function, find_most_frequent_words to find:
#    a) The ten most frequent words used in [Obama's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/obama_speech.txt)
#    b) The ten most frequent words used in [Michelle's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/michelle_obama_speech.txt)
#    c) The ten most frequent words used in [Trump's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/donald_speech.txt)
#    d) The ten most frequent words used in [Melina's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/melina_trump_speech.txt)

speeches = {
    'DT_speech': './donald_speech.txt',
    'BO_speech': './obama_speech.txt',
    'MT_speech': './melina_trump_speech.txt',
    'MO_speech': './michelle_obama_speech.txt'
}

for speech_name, speech_location in speeches.items():
    with open(speech_location, 'r', encoding='utf-8') as k:
        print(speech_location.split('/')[1], ': \t', find_most_common_words(k.read(), 10))

# 7. Write a python application that checks similarity between two texts.
#   It takes a file or a string as a parameter and it will evaluate the
#   similarity of the two texts. For instance check the similarity between the
#   transcripts of [Michelle's](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/michelle_obama_speech.txt)
#   and [Melina's](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/melina_trump_speech.txt) speech.
#   You may need a couple of functions, function to clean the text(clean_text),
#   function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity).
#   List of [stop words](httpm:/mgithub.com/Asabeneh/30-Days-Of-Python/blob/master/data/stop_words.py) are in the data directory


def get_words_from_text(text):
    """Returns a list of pure words"""
    translation_table = str.maketrans(string.punctuation+string.ascii_uppercase,
                                      " "*len(string.punctuation)+string.ascii_lowercase)
    trans_text = text.translate(translation_table)

    return trans_text.split()


def get_word_freq(word_lst):
    """Returns a dictionary of word : word counts"""
    dict = {}

    for word in word_lst:
        if word in dict:
            dict[word] = dict[word] + 1
        else:
            dict[word] = 1

    return dict


def dot_product(data1, data2):
    """Returns the Dot product of two lists"""
    dot_sum = 0.0

    for key in data1:

        if key in data2:
            print(key)
            dot_sum += (data1[key] * data2[key])
    return dot_sum


def vector_angle(data1, data2):
    """Returns the vector angle of two data sets"""
    numerator = dot_product(data1, data2)
    denominator = math.sqrt(dot_product(data1, data1)*dot_product(data2, data2))
    return math.acos(numerator / denominator)


def text_similarity(text1, text2):
    """Gets list of words, passes that to a count,
    gets similarity between them."""

    word_list1 = get_words_from_text(text1)
    word_list2 = get_words_from_text(text2)

    word_freq_list1 = get_word_freq(word_list1)
    word_freq_list2 = get_word_freq(word_list2)

    print(word_freq_list1, word_freq_list2)

    distance = vector_angle(word_freq_list1, word_freq_list2)

    return distance


dt_speech = read_file(speeches['DT_speech'])
bo_speech = read_file(speeches['BO_speech'])

print("The similarity index between {} and {} is {:.6f} (radians)".format(
    speeches['DT_speech'], speeches['BO_speech'],
      text_similarity(dt_speech, bo_speech)))


# 8. Find the 10 most repeated words in the romeo_and_juliet.txt

rnj_lines = read_file('./romeo_and_juliet.txt')
rnj_words = get_words_from_text(rnj_lines)

print(find_most_common_words(rnj_words, 10))


# 9. Read the [hacker news csv](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/hacker_news.csv) file and find out:
#    a) Count the number of lines containing python or Python
#    b) Count the number lines containing JavaScript, javascript or Javascript
#    c) Count the number lines containing Java and not JavaScript

def countRegEx(csv_Obj,regEx):
    csv_reader = csv.reader(csv_Obj, delimiter=',')
    count = 0
    for row in csv_reader:
        for i in row:
            count += len(re.findall(regEx,i))

    csv_Obj.seek(0) #Reset back to start of file
    return count

with open('./hack_news.csv','r') as f:
    print(countRegEx(f, r'[Pp]ython'))
    print(countRegEx(f, r'Java'))
    print(countRegEx(f, r'Java[Ss]cript'))


# ### Exercises: Level 3
