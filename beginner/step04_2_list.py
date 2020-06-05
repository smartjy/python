courses1 = ['History', 'Math', 'Physics', 'development']

for item in courses1:
    print('items =', item)

print('')

# index start with 0
for index, courses1 in enumerate(courses1):
    print('index =', index, courses1)

print('')

# index start with 1
courses1 = ['History', 'Math', 'Physics', 'development']
for index, courses1 in enumerate(courses1, start=1):
    print('index =', index, courses1)

print('#######################################################################################')

courses1 = ['History', 'Math', 'Physics', 'development']
courses1_str1 = ', '.join(courses1)
courses1_str2 = ' - '.join(courses1)

print(courses1_str1)
print(courses1_str2)

new_list = courses1_str2.split(' - ')
print(new_list)
