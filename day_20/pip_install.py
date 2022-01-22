#! /usr/bin/env python3
import string
import statistics
import json
import requests
from mypackages import arithmetic



def get_words_from_text(text):
    """Returns a list of pure words"""
    translation_table = str.maketrans(string.punctuation+string.ascii_uppercase,
                                      " "*len(string.punctuation)+string.ascii_lowercase)
    trans_text = text.translate(translation_table)

    return trans_text.split()


def most_freq_words(word_list, freq_count=-1):
    """Returns x most frequest words,
    if count not provide then returns all.
    returns list of tuple counts"""

    word_dict = {}

    for word in word_list :
        if word in word_dict:
            word_dict[word] = word_dict[word] + 1
        else:
            word_dict[word] = 1

    return sorted(word_dict.items(), key=lambda x: x[1],
                  reverse=True)[:freq_count]


def url_text_ten_freq(url):
    """Prints the 10 most frequent words from a url"""
    response = requests.get(url)

    url_text = response.text

    url_word_list = get_words_from_text(url_text)
    url_ten_most = most_freq_words(url_word_list, 10)

    print(url_ten_most)


def json_api_to_dict(url):
    """Takes in a url and converts returns it in dictionary format"""
    response = requests.get(url)

    json_dict = json.loads(response.text)

    return json_dict


def get_min_weight(cat_dict):
    """Takes in the cat API as a dictionary, iterates through the values
    Then returns the min metric weight found"""
    min_weight = 0
    for cat in cat_dict:
        # Value is a range i.e '3 - 5', we take the 1 elemtn in that split
        cat_min = int(cat['weight']['metric'].split()[0])

        if cat_min < min_weight or min_weight == 0:
            min_weight = cat_min

    return min_weight


def get_max_weight(cat_dict):
    """Takes in the cat API as a dictionary, iterates through the values
    Then returns the max metric weight found"""
    max_weight = 0
    for cat in cat_dict:
        # Dict is a range i.e '3 - 5', we take the 3 element in that split
        cat_max = int(cat['weight']['metric'].split()[2])

        if cat_max > max_weight:
            max_weight = cat_max

    return max_weight


def get_mean_weight(cat_dict):
    """Finds the mean weight from the provided cat API dict
       Takes the mean of each weight, combines into a list,
       then takes mean of entire list, returns the result"""

    mean_list = []
    cat_mean = 0

    for cat in cat_dict:
        # Take the first and last element of cat weight
        # Use to find mean, add result to mean_list
        lower_weight, *__, upper_weight = cat['weight']['metric'].split()

        # mean = sum of parts / length
        mean_list.append(arithmetic.mean(int(lower_weight), int(upper_weight)))

    cat_mean = arithmetic.mean(*mean_list)
    return cat_mean


def get_weight_list(cat_dict):
    """Returns a list of sorted weights"""
    weight_list = []

    for cat in cat_dict:
        lower_weight, *__, upper_weight = cat['weight']['metric'].split()

        weight_list += [int(lower_weight), int(upper_weight)]

    return sorted(weight_list)


def get_median_weight(cat_dict):
    """Gets the median weight from the cat_Dict list"""
    weight_list = get_weight_list(cat_dict)

    median_weight = statistics.median(weight_list)

    return median_weight


def get_stdev_weight(cat_dict):
    """Returns the standard deviation in weight for the cats"""
    weight_list = get_weight_list(cat_dict)
    stdev_weight = statistics.stdev(weight_list)

    return stdev_weight


def get_min_life(cat_dict):
    """Takes in the cat API as a dictionary, iterates through the values
    Then returns the min metric life found"""
    min_life = 0
    for cat in cat_dict:
        # Value is a range i.e '3 - 5', we take the 1 elemtn in that split
        cat_min = int(cat['life_span'].split()[0])

        if cat_min < min_life or min_life == 0:
            min_life = cat_min

    return min_life


def get_max_life(cat_dict):
    """Takes in the cat API as a dictionary, iterates through the values
    Then returns the max metric life found"""
    max_life = 0
    for cat in cat_dict:
        # Dict is a range i.e '3 - 5', we take the 3 element in that split
        cat_max = int(cat['life_span'].split()[2])

        if cat_max > max_life:
            max_life = cat_max

    return max_life


def get_mean_life(cat_dict):
    """Finds the mean life from the provided cat API dict
       Takes the mean of each life, combines into a list,
       then takes mean of entire list, returns the result"""

    mean_list = []
    cat_mean = 0

    for cat in cat_dict:
        # Take the first and last element of cat life
        # Use to find mean, add result to mean_list
        lower_life, *__, upper_life = cat['life_span'].split()

        # mean = sum of parts / length
        mean_list.append(arithmetic.mean(int(lower_life), int(upper_life)))

    cat_mean = arithmetic.mean(*mean_list)
    return cat_mean


def get_life_list(cat_dict):
    """Returns a list of sorted lifes"""
    life_list = []

    for cat in cat_dict:
        lower_life, *__, upper_life = cat['life_span'].split()

        life_list += [int(lower_life), int(upper_life)]

    return sorted(life_list)


def get_median_life(cat_dict):
    """Gets the median life from the cat_Dict list"""
    life_list = get_life_list(cat_dict)

    median_life = statistics.median(life_list)

    return median_life


def get_stdev_life(cat_dict):
    """Returns the standard deviation in life for the cats"""
    life_list = get_life_list(cat_dict)
    stdev_life = statistics.stdev(life_list)

    return stdev_life


def get_cat_stats(cat_url):
    """Primary function to display cat stats for Exercise 2"""
    cat_dict = json_api_to_dict(cat_url)

    # Weight Variables and function Calls
    max_weight = get_max_weight(cat_dict)
    min_weight = get_min_weight(cat_dict)
    mean_weight = get_mean_weight(cat_dict)
    median_weight = get_median_weight(cat_dict)
    stdev_weight = get_stdev_weight(cat_dict)

    # Lifespan Variables & function calls
    max_life = get_max_life(cat_dict)
    min_life = get_min_life(cat_dict)
    mean_life = get_mean_life(cat_dict)
    median_life = get_median_life(cat_dict)
    stdev_life = get_stdev_life(cat_dict)

    print(f"Max Weight: \t{max_weight}")
    print(f"Min Weight: \t{min_weight}")
    print(f"Mean Weight: \t{mean_weight:.04f}")
    print(f'Median Weight: \t{median_weight}')
    print(f'Standard Deviation Weight: \t{stdev_weight}')
    print()
    print(f"Max life: \t{max_life}")
    print(f"Min life: \t{min_life}")
    print(f"Mean life: \t{mean_life:.04f}")
    print(f'Median life: \t{median_life}')
    print(f'Standard Deviation life: \t{stdev_life}')


def get_largest_countries(country_dict, ret_count=-1):
    """Returns the x largets countries by population"""
    pop_dict = {}
    for country in country_dict:
        pop_dict[country['name']['common']] = country['population']

    return sorted(pop_dict.items(), key=lambda x: x[1],
                  reverse=True)[:ret_count]


def get_most_spoken(country_dict, ret_count=-1):
    """Returns the x most spoken languages"""
    lang_dict = {}
    for country in country_dict:

        try:# Catches error if no languages listed
            for lang in country['languages'].values():
                if lang in lang_dict:
                    lang_dict[lang] += 1
                else:
                    lang_dict[lang] = 1
        except KeyError:
            print('No languages found for: ', country['name']['common'])
            continue

    return sorted(lang_dict.items(), key=lambda x: x[1],
                  reverse=True)[:ret_count]


def get_country_stats(country_url):
    """Primary function caller for Excercise 3"""
    country_dict = json_api_to_dict(country_url)

    ten_largest = get_largest_countries(country_dict, 10)
    ten_most_spoken = get_most_spoken(country_dict, 10)

    # calls get_most_spoke with no seccond arg to return all langs
    # Then gets len of returned dict
    total_languages = len(get_most_spoken(country_dict))

    print(f'Ten Largest: \t{ten_largest}')
    print(f'Ten Most Spoken: \t{ten_most_spoken}')
    print(f'Total Languages: \t{total_languages}')

# ## Exercises: Day 20
#
# 1. Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'


URL = 'http://www.gutenberg.org/files/1112/1112.txt'
url_text_ten_freq(URL)

# 2. Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
#    1. the min, max, mean, median, standard deviation of cats' weight in metric units.
#    2. the min, max, mean, median, standard deviation of cats' lifespan in years.
#    3. Create a frequency table of country and breed of cats


CAT_URL = 'https://api.thecatapi.com/v1/breeds'
get_cat_stats(CAT_URL)

# 3. Read the [countries API](https://restcountries.eu/rest/v2/all) and find
#    1. the 10 largest countries
#    2. the 10 most spoken languages
#    3. the total number of languages in the countries API

COUNTRIES_URL = 'https://restcountries.com/v3.1/all'
get_country_stats(COUNTRIES_URL)

# 4. UCI is one of the most common places to get data sets for data science and machine learning. Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php). Without additional libraries it will be difficult, so you may try it with BeautifulSoup4
