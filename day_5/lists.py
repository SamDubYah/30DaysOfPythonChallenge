#! /usr/bin/env python3 

### Exercises: Level 1

# 1. Declare an empty list
lst = []
print(lst)

# 2. Declare a list with more than 5 items
lst = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7']
print(lst)

# 3. Find the length of your list
print('Length: \t', len(lst))

# 4. Get the first item, the middle item and the last item of the list
print('First: \t\t',lst[0])
print('Middle: \t', lst[len(lst)//2])
print('Last: \t\t', lst[-1])

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Sam', 25, '6ft 3in', 'Single', {'address':'6735 Golden Briar'}]

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Print the list using _print()_
print(it_companies)

# 8. Print the number of companies in the list
print('Company Count: \t', len(it_companies))

# 9. Print the first, middle and last company
print('First Company: \t', it_companies[0])
print('Middle Company: ', it_companies[len(it_companies)//2])
print('Last Company: \t', it_companies[-1])

# 10. Print the list after modifying one of the companies
it_companies[4] = 'Twitter'
print('Changed List: \t', it_companies)

# 11. Add an IT company to it_companies
it_companies.append('Coalfire')
print('Appended list: \t', it_companies)

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(3, 'FireEye')
print('Inserted list: \t', it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print('Upper\'d List: \t', it_companies)

# 14. Join the it_companies with a string '#; '
print('Joined List: \t','#; '.join(it_companies))

# 15. Check if a certain company exists in the it_companies list.
print('GOOGLE Exist: \t', 'GOOGLE' in it_companies)

# 16. Sort the list using sort() method
it_companies.sort()
print('Sorted List: \t', it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print('Reversed List: \t', it_companies)

# 18. Slice out the first 3 companies from the list
print('Sliced List: \t', it_companies[:3])

# 19. Slice out the last 3 companies from the list
print('Sliced List2: \t', it_companies[-3:])

# 20. Slice out the middle IT company or companies from the list
print('Middle Slice: \t', it_companies[len(it_companies)//2])

# 21. Remove the first IT company from the list
it_companies.pop(0)
print('First Remove: \t', it_companies)

# 22. Remove the middle IT company or companies from the list
it_companies.pop(len(it_companies)//2)
print('Middle Remove: \t', it_companies)

# 23. Remove the last IT company from the list
it_companies.pop(-1)
print('Last Remove: \t', it_companies)

# 24. Remove all IT companies from the list
it_companies.clear()
print('Cleared List: \t', it_companies)

# 25. Destroy the IT companies list
del it_companies


# 26. Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined = front_end + back_end

print('Joined Lists: \t', joined)

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = joined.copy()
print('Full Stack: \t', full_stack)

# ### Exercises: Level 2

# 1. The following is a list of 10 students ages:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]


# - Sort the list and find the min and max age
ages.sort()
print('Min Age: \t', ages[0])
print('Max Age: \t', ages[-1])

# - Add the min age and the max age again to the list
ages.insert(0,ages[0])
ages.insert(-1,ages[-1])
print('Ages List: \t', ages)

# - Find the median age (one middle item or two middle items divided by two)
age_median = len(ages) // 2
print('Median Age: \t', ages[age_median])

# - Find the average age (sum of all items divided by their number )
age_sum = 0

for ele in range(0, len(ages)):
    age_sum += ages[ele]

age_avg = age_sum / len(ages)

print('Average Age: \t', age_avg)

# - Find the range of the ages (max minus min)
age_rang = ages[-1] - ages[0]
print('Range of Age: \t', age_rang)

# - Compare the value of (min - average) and (max - average), use _abs()_ method
print('Abs of Min: \t', abs(ages[0] - age_avg))
print('Abs of Max: \t', abs(ages[-1] - age_avg))

# 1. Find the middle country(ies) in the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/tree/master/data/countries.py)
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

def middleList(input_list):
    middle = float(len(input_list)/2)
    if middle %2 != 0: # If length of list is odd, print both sides
        return input_list[int(middle)]
    else: 
        return input_list[int(middle) - 1], input_list[int(middle)]

print('Middle List: \t', middleList(countries))

# 1. Divide the countries list into two equal lists if it is even if not one more country for the first half.
def splitList(input_list):
    mid_ele = middleList(input_list) # Git the mid points
    
    if type(mid_ele) == tuple:
        # First half of list, from 0th ele to index of mid_ele + 1 --- adding 1 to include mid_ele
        first_half = input_list[:input_list.index(mid_ele[0])+1]
        second_half = input_list[input_list.index(mid_ele[1]):] # Start from second mid_ele to ned

        return first_half, second_half
        
    else:
        #Same reasoning as above, +1 to include element
        first_half = input_list[:input_list.index(mid_ele) + 1]
        second_half = input_list[input_list.index(mid_ele)+1:] # Adding 1 here to not include mid_ele

        return first_half, second_half

#Pass Large Countries list to splitList Function
first_half, second_half = splitList(countries)
print('Len of First: \t', len(first_half))
print('Len of Second: \t', len(second_half))

# 1. Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

CHI, RUS, USA, *scadic = countries

print('Unpacked CHI: \t', CHI)
print('Unpacked RUS: \t', RUS)
print('Unpacked USA: \t', USA)
print('Unpacked Other: ', scadic) 
