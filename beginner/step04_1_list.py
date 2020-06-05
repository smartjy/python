courses1 = ['History', 'Math', 'Physics', 'development']

print('courses1 is =', courses1)
print('courses1 length =', len(courses1))
print('courses1 index 0 =', courses1[0])
print('courses1 index 1 =', courses1[1])
print('courses1 index 3 =', courses1[3])
print('courses1 last index =', courses1[-1])
print('courses1 index 0 to 2 =', courses1[0:2])
print('courses1 index first to 3 =', courses1[:3])
print('courses1 index 2 to lst =', courses1[2:])

courses1.append('Art')
print('courses1 append Art =', courses1)

courses1.insert(0, 'Art')
print('courses1 insert index [0] Art =', courses1[:5])
print('#######################################################################################')

courses1 = ['History', 'Math', 'Physics', 'development']
courses2 = ['Computer', 'Science']

courses1.insert(5, courses2)
print('courses1 insert =', courses1)
print('courses1 last index =', courses1[-1])
print('courses1 index 3 =', courses1[3])
print('courses1 index 4 =', courses1[4])
print('#######################################################################################')

courses1 = ['History', 'Math', 'Physics', 'development']
courses2 = ['Computer', 'Science']

courses1.extend(courses2)
print('courses1 extend =', courses1)
print('#######################################################################################')

courses1 = ['History', 'Math', 'Physics', 'development']
popped = courses1.pop()
print('popped =', popped)
print('courses1 pop =', courses1)
print('#######################################################################################')

courses1 = ['History', 'Math', 'Physics', 'development']
courses1.reverse()
print('courses1 reverse =', courses1)
print('#######################################################################################')

courses1 = ['History', 'Math', 'Physics', 'development']
courses1.remove('History')
print('courses1 remove =', courses1)
print('#######################################################################################')

sort_test1 = ['ccc', 'aaa', 'ddd', 'bbb']
sort_test2 = [2, 1, 4, 3]
sort_test1.sort()
sort_test2.sort()
print('alphabets sort =', sort_test1)
print('numbers sort =', sort_test2)

sorted(sort_test1)
print('alphabets sorted =', sort_test1)
sorted(sort_test2)
print('numbers sorted =', sort_test2)

sort_test1.sort(reverse=True)
sort_test2.sort(reverse=True)
print('alphabets reverse order =', sort_test1)
print('numbers reverse order =', sort_test2)
print('#######################################################################################')

str_test1 = ['ccc', 'aaa', 'ddd', 'bbb']
num_test1 = [2, 1, 4, 3]

print('alphabets MIN =', min(num_test1))
print('alphabets MAX =', max(num_test1))
print('numbers MIN =', min(num_test1))
print('numbers MAX =', max(num_test1))
print('numbers SUM =', sum(num_test1))
print('#######################################################################################')

courses1 = ['History', 'Math', 'Physics', 'development']

print('courses1 Math index = ', courses1.index('Math'))
print('courses1 Physics index = ', courses1.index('Physics'))
print('is courses1 in Math?', 'Math' in courses1)
print('is courses1 in Computer?', 'Computer' in courses1)

