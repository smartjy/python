# install python3

# using pycharm ide

# pycharm set env python automatically

# 문자열
text = 'hello'
print(text.upper())
print(text.count('l'))

# 논리형 (True or False)
print(100 < 200)
print(100 == 200)

# 리스트형
public = ['AWS', 'Azure', 'GCP']
private = ['kubernetes', 'openshift']

# 사전형 (key, value)
myphone = {'apple':'Iphone', 'samsung':'Galaxy', 'lg':'Velvet'}
print(myphone['apple'])
print(myphone.keys())
print(myphone.values())

# 튜플(tuple) like group?
tuple_var = ('apple', 'expensive', 155)
print(tuple_var[0],tuple_var[1])
print(tuple_var)

# 1 집합형(set)
computer1 = {'mac', 'windows', 'linux'}
print(computer1)

# 2 집합형(set function)
computer2 = set('operating')
print(computer2)

# Deduplication
fruits = ['apple', 'orange', 'melon', 'kiwi', 'apple', 'melon']
fruits_set = set(fruits)
print(fruits_set)
