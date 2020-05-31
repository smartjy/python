language = ['Java', 'Python', 'Go', 'Bash']
language[0] = 'Java Script'
language.append('c++')
language.remove('Bash')
print('Programing languages :', language)


employee = {'name':'Jay', 'age':32, 'department':'RnD'}
print('Emp Name :', employee['name'])
print('Emp Age :', employee['age'])
print('Emp Dept :', employee['department'])

print(employee.keys())
print(employee.values())

pc_os = ('Mac', 'Windows', 'Linux')
# pc_os[2] = 'Ubuntu'
print('PC Operation System :', pc_os)


city1 = {'Seoul', 'Busan', 'Gwangju', 'Seoul'}
city2 = {'Seoul', 'Daegu', 'Gwangju', 'Incheon'}
# print('City of Korea: ', city)
# print('Set Method :', set(language))
print(city1 & city2)
print(city1 - city2)
print(city2 - city1)