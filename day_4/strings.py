#!/usr/bin/env python3

# 1
string_to_cat = 'Thirty '+ 'Days '+ 'Of '+ 'Python'

# 2
string2_to_cat = 'Coding ' + 'For ' + 'All'

# 3
company = "Coding For All"

# 4
print(company)

# 5
print(len(company))

# 6
print(company.upper())

# 7
print(company.lower())

# 8
print(company.capitalize())
print(company.swapcase()) 
print(company.title())

# 9 - Print the first word of the string
print(company[0:company.index(' ')])

# 10 - If coding exists in string print 'Coding Found!' else 'Not Found'
if(company.find('Coding') != '0'):
    print('Coding Found!')
else:
    print('Not Found')

# 11 - Replace Coding with Python
print(company.replace('Coding', 'Python'))

# 12 - Replace Everyone with all
print('Python for Everyone'.replace('Everyone', 'All'))

# 13 - just split
print('Coding For All'.split())

# 14 - Split by comma
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(', '))

# 15 - Print the first index of the string
print('Coding For All'[0])

# 16 - What is the last index of the string
print(len('Coding For All')-1)

# 17
print('Coding For All'[10])

# 18 - Create an Acronym
PFE = 'Python For Everyone'
print ("".join(e[0] for e in PFE.split()))

# 19 ^^^
CFA = 'Coding For All'
print ("".join(e[0] for e in CFA.split()))

# 20
print(CFA.index('C'))

# 21
print(CFA.index('F'))

# 22
print((CFA + 'People').rindex('l'))

# 23
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))

# 24 - Using sentence from 23
print(sentence.rindex('because'))

# 25 - Using sentence from 23
to_remove = 'because because because '
print(len(sentence))
print("Sentence Slicing: ",sentence[0:sentence.index(to_remove)] + sentence[sentence.rindex(to_remove) + len(to_remove):])

# 26 - Duplicate of 23
print(sentence.find('because'))

# 27 - Duplicate of 25

# 28
print(CFA.startswith('Coding'))

# 29
print(CFA.startswith('coding'))

# 30
print('   Coding For All      '.strip())

# 31
print('30DaysOfPython'.isidentifier())
print('thiry_days_of_python'.isidentifier())

# 32
py_libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(py_libs))

# 33
print( "I am enjoying this challenge. \nI just wonder what is next.")

# 34
print("Name \tAge \tCountry \tCity\nAsabeneh \t250 \tFinland \tHelsinki".expandtabs(5))

# 35
radius = 10
area = 3.14 * radius ** 2

print(f'The area of a circle with a radius of {radius} meters is {area} meters sqaured')

# 36
a = 8
b = 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # Limit 2 places after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))
