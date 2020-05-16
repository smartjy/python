import step09_module
import step09_module as sm
from step09_module import find_index, test

courses = ['History', 'Math', 'Physics', 'CompSci']

index1 = step09_module.find_index(courses, 'Math')
print('Index1 :', index1, '\n')

index2 = sm.find_index(courses, 'CompSci')
print('Index2 :', index2, '\n')

index3 = find_index(courses, 'History')
print('Index3 :', index3, '\n')

print('module test variable :', test)
