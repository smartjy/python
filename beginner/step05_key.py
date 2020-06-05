employee = {'name': 'Jay', 'age': 35, 'department': ['engineer', 'developer']}

print('employee info :', employee)
print('employee name :', employee['name'])
print('employee department :', employee['department'])
print('employee age :', employee.get('age'))
print('employee phone :', employee.get('phone', 'Not Found'))

employee.update({'name': 'Tom', 'age': 26})
print('employee update :', employee)

del employee['department']
print('employee del :', employee)

age = employee.pop('age')
print('employee pop :', employee)

employee = {'name': 'Jay', 'age': 35, 'department': ['engineer', 'developer']}
print('employee value :', employee.values())

print('employee items :', employee.items())

print('')
for key in employee:
    print('employee key :', key)
print('')

for key, value in employee.items():
    print('employee key,value :', key, value)