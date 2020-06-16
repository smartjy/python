languge = {1:'Java', 2:'Go', 3:'Python'}
print('languge Dictionary:', languge)
print('languge Dictionary 3:', languge[3])
print('languge Dictionary get 1:', languge.get(1))
print('languge Dictionary get 5:', languge.get(5, 'What Languge?'))

print('languge 2?', 2 in languge)
print('languge 4?', 4 in languge)

languge[4] = 'Bash'
print('Index[4](Bash) Add', languge)

del languge[2]
print('del index 2:', languge)

print('languge keys:', languge.keys())
print('languge values:', languge.values())
print('languge items:', languge.items())

print(languge.clear())