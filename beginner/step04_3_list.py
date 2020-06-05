# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {}
empty_set = set()

# Mutable
list_1 = ['History', 'Math', 'Physics', 'Development']
list_2 = list_1

print(list_1)
print(list_2)
print('')

list_1[0] = 'Computer'
print(list_1)
print(list_2)
print('')

# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'Development')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)
print('')

# Doesn't work
# tuple_1[0] = 'Computer'
#
# print(tuple_1)
# print(tuple_2)
# print('')

# Sets
cs_courses = {'History', 'Math', 'Physics', 'Development', 'Development'}
print(cs_courses)

courses1 = {'History', 'Math', 'Physics', 'Development'}
courses2 = {'Architect', 'Math', 'Science', 'Development'}

print('courses1 and courses2 intersection =', courses1.intersection(courses2))
print('courses1 and courses2 difference =', courses1.difference(courses2))
print('courses1 and courses2 union =', courses1.union(courses2))