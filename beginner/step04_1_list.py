courses1 = ['History', 'Math', 'Physics', 'development']

print('courses1 is ='.__str__(), courses1)
print('courses1 length =', len(courses1))
print('courses1 index 0 ='.__str__(), courses1[0])
print('courses1 index 1 ='.__str__(), courses1[1])
print('courses1 index 3 ='.__str__(), courses1[3])
print('courses1 last index ='.__str__(), courses1[-1])
print('courses1 index 0 to 2 ='.__str__(), courses1[0:2])
print('courses1 index first to 3 ='.__str__(), courses1[:3])
print('courses1 index 2 to lst ='.__str__(), courses1[2:])

courses1.append('Art')
print('courses1 append Art ='.__str__(), courses1)

courses1.insert(0, 'Art')
print('courses1 insert index [0] Art ='.__str__(), courses1[:5])
print('#######################################################################################')

courses1 = ['History', 'Math', 'Physics', 'development']
courses2 = ['Computer', 'Science']

courses1.insert(5, courses2)
print('courses1 insert ='.__str__(), courses1)
print('courses1 last index ='.__str__(), courses1[-1])
print('courses1 index 3 ='.__str__(), courses1[3])
print('courses1 index 4 ='.__str__(), courses1[4])
print('#######################################################################################')

courses1 = ['History', 'Math', 'Physics', 'development']
courses2 = ['Computer', 'Science']

courses1.extend(courses2)
print('courses1 extend ='.__str__(), courses1)
print('#######################################################################################')

courses1 = ['History', 'Math', 'Physics', 'development']
popped = courses1.pop()
print('popped ='.__str__(), popped)
print('courses1 pop ='.__str__(), courses1)
print('#######################################################################################')

courses1 = ['History', 'Math', 'Physics', 'development']
courses1.reverse()
print('courses1 reverse ='.__str__(), courses1)
print('#######################################################################################')

courses1 = ['History', 'Math', 'Physics', 'development']
courses1.remove('History')
print('courses1 remove ='.__str__(), courses1)
print('#######################################################################################')

sort_test1 = ['ccc', 'aaa', 'ddd', 'bbb']
sort_test2 = [2, 1, 4, 3]
sort_test1.sort()
sort_test2.sort()
print('alphabets sort ='.__str__(), sort_test1)
print('numbers sort ='.__str__(), sort_test2)

sorted(sort_test1)
print('alphabets sorted ='.__str__(), sort_test1)
sorted(sort_test2)
print('numbers sorted ='.__str__(), sort_test2)

sort_test1.sort(reverse=True)
sort_test2.sort(reverse=True)
print('alphabets reverse order ='.__str__(), sort_test1)
print('numbers reverse order ='.__str__(), sort_test2)
print('#######################################################################################')

str_test1 = ['ccc', 'aaa', 'ddd', 'bbb']
num_test1 = [2, 1, 4, 3]

print('alphabets MIN ='.__str__(), min(num_test1))
print('alphabets MAX ='.__str__(), max(num_test1))
print('numbers MIN ='.__str__(), min(num_test1))
print('numbers MAX ='.__str__(), max(num_test1))
print('numbers SUM ='.__str__(), sum(num_test1))
print('#######################################################################################')

courses1 = ['History', 'Math', 'Physics', 'development']

print('courses1 Math index = '.__str__(), courses1.index('Math'))
print('courses1 Physics index = '.__str__(), courses1.index('Physics'))
print('is courses1 in Math?'.__str__(), 'Math' in courses1)
print('is courses1 in Computer?'.__str__(), 'Computer' in courses1)

