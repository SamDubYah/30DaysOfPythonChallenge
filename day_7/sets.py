#! /usr/bin/env python3

# ## 💻 Exercises: Day 7


# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


# ### Exercises: Level 1

# 1. Find the length of the set it_companies
print('Set Length: \t', len(it_companies))

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print('Twitter Added: \t', it_companies)

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Cisco', 'Tenable', 'Geenbone'])
print('Multi Add: \t', it_companies)

# 4. Remove one of the companies from the set it_companies
it_companies.remove('IBM')
print('IBM Removed: \t', it_companies)

# 5. What is the difference between remove and discard
#Discard does not raise any error when the item is not found

# ### Exercises: Level 2

# 1. Join A and B
joined = A.union(B)
print('Joined A + B: \t', joined)

# 1. Find A intersection B
intersect = A.intersection(B)
print('Intersection: \t', intersect)

# 1. Is A subset of B
print('A sub of B? \t', A.issubset(B))

# 1. Are A and B disjoint sets
print('A & B Disjoint?\t', A.isdisjoint(B))

# 1. Join A with B and B with A
AwithB = A.union(B)
BwithA = B.union(A)
print('A with B: \t', AwithB)
print('B with A: \t', BwithA)

# 1. What is the symmetric difference between A and B
print('Symm Diff: \t', A.symmetric_difference(B))

# 1. Delete the sets completely
del A, B

# ### Exercises: Level 3

# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_st = set(age)
print('Age List Len: \t', len(age))
print('Age Set Len: \t', len(age_st))

# 1. Explain the difference between the following data types: string, list, tuple and set
### String: a mutable conjoined list of characters (Essentially just a list with single characters)
### list: a mutable collection ordered items
### tuple: an imutable collection of ordered items
### set: a mutable collection of unordered items

# 2. _I am a teacher and I love to inspire and teach people._ How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people.'

print('Unique Count: \t', len(set(sentence.split(' '))))