employee = {'name': 'Jay', 'age': 35, 'department': ['engineer', 'developer']}

print('employee info :'.__str__(), employee)
print('employee name :'.__str__(), employee['name'])
print('employee department :'.__str__(), employee['department'])
print('employee age :'.__str__(), employee.get('age'))
print('employee phone :'.__str__(), employee.get('phone', 'Not Found'))

employee.update({'name': 'Tom', 'age': 26})
print('employee update :'.__str__(), employee)

del employee['department']
print('employee del :'.__str__(), employee)

age = employee.pop('age')
print('employee pop :'.__str__(), employee)

employee = {'name': 'Jay', 'age': 35, 'department': ['engineer', 'developer']}
print('employee value :'.__str__(), employee.values())

print('employee items :'.__str__(), employee.items())

print('')
for key in employee:
    print('employee key :'.__str__(), key)
print('')

for key, value in employee.items():
    print('employee key,value :'.__str__(), key, value)