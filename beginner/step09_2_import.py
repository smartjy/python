import sys
import random
import math
import datetime
import calendar
import os
# sys.path.append('') # If does not same directory module file, add module file directory right here

# print(sys.path)

courses = ['History', 'Math', 'Physics', 'CompSci']

random_courses = random.choice(courses)
print('Random courses :', random_courses, '\n')

rads = math.radians(90)
print('Radians courses :', rads, '\n')

today = datetime.date.today()
print('Today is', today, '\n')
print('2020 year leap :', calendar.isleap(2020), '\n')

print('OS getcwd :', os.getcwd(), '\n')
print('Reference File :', os.__file__, '\n')
