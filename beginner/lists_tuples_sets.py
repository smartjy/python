courses = ['History', 'Math', 'Physics', 'ComSci']
# courses1 = ['Art', 'Education']

print('###', courses[1])
print(courses)
print(len(courses))

# print(courses[0])
# print(courses[3])
# print(courses[1:])
# print(courses[1:3])


# courses.append('Art')
# courses.insert(0, 'Art')
# courses.extend('History')
# courses.extend(courses1)
# courses.append(courses1)
# courses.pop()
# courses.remove('ComSci')

# courses.sort()
# courses.reverse()
# sorted(courses)
print(courses.index('Physics'))

print(courses)

# print('Art' in courses)
# print('Math' in courses)

# append ['History', 'Math', 'Physics', 'ComSci', 'Art']
# insert ['Art', 'History', 'Math', 'Physics', 'ComSci']
# extend ['History', 'Math', 'Physics', 'ComSci', 'H', 'i', 's', 't', 'o', 'r', 'y']
# extend ['History', 'Math', 'Physics', 'ComSci', 'Art', 'Education']
# append ['History', 'Math', 'Physics', 'ComSci', ['Art', 'Education']]
# pop ['History', 'Math', 'Physics']

for i in courses:
    print(i)

for index, course in enumerate(courses, start=1):
    print(index, course)

courses_str = ' '.join(courses)

print(courses_str)

new_list = courses_str.split(' ')

print(new_list)

print('\n#### Tuple ####\n')
print('\n#### Sets ####\n')

st_courses = {'History', 'Math', 'Physics', 'ComSci'}
print(st_courses)
