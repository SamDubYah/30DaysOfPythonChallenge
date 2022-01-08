#!/usr/bin/env python3

# 1. Create  an empty dictionary called dog
dog = {}
print ('Empty Dict: \t', len(dog))
# 2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Blue'
dog['color'] = 'Blue'
dog['breed'] = 'Weimaranner'
dog['legs'] = 4
dog['age'] = 3

print('Dog Dict: \t', dog)

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {'first_name':'Sam', 'last_name':'Warner','gender':'Male','age':'25','marital_status':'single','skills':'computer hacking','country':'USA','city':'Colo Springs','address':'6735 Golden briar ln'}

# 4. Get the length of the student dictionary
print('Dict Length: \t', len(student))

# 5. Get the value of skills and check the data type, it should be a list
print('Skills: \t', student['skills'])

# 6. Modify the skills values by adding one or two skills
student['skills'] = [student['skills'], 'exploitation', 'num-chucks']

print('Skills: \t', student['skills'])
print('Student: \t', student)

# 7. Get the dictionary keys as a list
print('Student Keys: \t', student.keys())

# 8. Get the dictionary values as a list
print('Student Values: \t', student.values())

# 9. Change the dictionary to a list of tuples using _items()_ method
student_t = (student.items())

print('Studen Tuple: \t', student_t)

# 10. Delete one of the items in the dictionary
student.pop('address')

print('Studen Popped: \t', student)

# 11. Delete one of the dictionaries
del student
print('Student Deleted: \t')

