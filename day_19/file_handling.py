#! /usr/bin/env python3
import re
import json
import csv


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
print("Melina Trump speech line count: \t", count_lines("./day_19/melina_trump_speech.txt"))
print("Donald Trump speech line count: \t", count_lines("./day_19/donald_speech.txt"))
print("Barrack Obama speech line count: \t",count_lines("./day_19/obama_speech.txt"))
print("Michelle Obama speech line count: \t",count_lines("./day_19/michelle_obama_speech.txt"))

print("Melina Trump speech word count: \t", count_words("./day_19/melina_trump_speech.txt"))
print("Donald Trump speech word count: \t", count_words("./day_19/donald_speech.txt"))
print("Barrack Obama speech word count: \t",count_words("./day_19/obama_speech.txt"))
print("Michelle Obama speech word count: \t",count_words("./day_19/michelle_obama_speech.txt"))

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

print(*most_spoken_languages("./day_19/countries_data.json", 10), sep="\n")
print()

#    # Your output should look like this
#    print(most_spoken_languages(filename='./data/countries_data.json', 3))
#    [(91, 'English'),
#    (45, 'French'),
#    (25, 'Arabic')]
#    ```
print(*most_spoken_languages('./day_19/countries_data.json', 3), sep="\n")


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

print(*most_populated_countries('./day_19/countries_data.json', 3), sep='\n')
print()
print(*most_populated_countries('./day_19/countries_data.json', 10), sep='\n')


# ### Exercises: Level 2

# 4. Extract all incoming email addresses as a list from the email_exchange_big.txt file.
def get_from_addresses(email_txtObj):
    data = email_txtObj.read() 
    emails = set([x for x in re.findall('([a-z\.]+@[a-z\.]+)', data) if 'localhost' not in x]) #Return list of emails excluding items containing 'localhost'
    return emails

with open('./day_19/email_exchange_big.txt','r') as f:
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
def find_most_common_words(txt, comCount):
    wc_dict = {}
    words = re.findall('[\w\d]+',txt)
    for i in words:
        if i in wc_dict.keys():
            wc_dict[i] += 1
        else:
            wc_dict[i] = 1

    return sorted([(v,k) for k,v in wc_dict.items()][:comCount],reverse=True)

with open('./day_19/email_exchange_big.txt','r') as f:
    print(find_most_common_words(f.read(), 10))

# 6. Use the function, find_most_frequent_words to find:
#    a) The ten most frequent words used in [Obama's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/obama_speech.txt)
#    b) The ten most frequent words used in [Michelle's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/michelle_obama_speech.txt)
#    c) The ten most frequent words used in [Trump's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/donald_speech.txt)
#    d) The ten most frequent words used in [Melina's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/melina_trump_speech.txt)

speeches = {
    'DT_speech':'./day_19/donald_speech.txt', 
    'BO_speech':'./day_19/obama_speech.txt',
    'MT_speech':'./day_19/melina_trump_speech.txt',
    'MO_speech':'./day_19/michelle_obama_speech.txt'
}

for k,v in speeches.items():
    with open(v, 'r') as k:
        print(v.split('/')[2],': \t',find_most_common_words(k.read(), 10))

# 7. Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of [Michelle's](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/michelle_obama_speech.txt) and [Melina's](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/melina_trump_speech.txt) speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of [stop words](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/stop_words.py) are in the data directory
# 8. Find the 10 most repeated words in the romeo_and_juliet.txt

with open('./day_19/romeo_and_juliet.txt') as f:
    print('Romeo And Juliet: \t', find_most_common_words(f.read(), 10))

# 9. Read the [hacker news csv](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/hacker_news.csv) file and find out:
#    a) Count the number of lines containing python or Python
#    b) Count the number lines containing JavaScript, javascript or Javascript
#    c) Count the number lines containing Java and not JavaScript

def count_regEx(csv_Obj,regEx):
    csv_reader = csv.reader(csv_Obj, delimiter=',')
    count = 0
    for row in csv_reader:
        for i in row:
            count += len(re.findall(regEx,i))

    csv_Obj.seek(0) #Reset back to start of file
    return count

with open('./day_19/hack_news.csv','r') as f:
    print(count_regEx(f, r'[Pp]ython'))
    print(count_regEx(f, r'Java'))    
    print(count_regEx(f, r'Java[Ss]cript'))


# ### Exercises: Level 3