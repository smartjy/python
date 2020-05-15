# Print message
print('hello python world')

first_msg = 'This is first string variable'

print (first_msg)
print (len(first_msg))
print (first_msg[0])
print (first_msg[1])
print (first_msg[0:4])
print (first_msg[:4])
print (first_msg[7:])
print (first_msg.lower())
print (first_msg.upper())
print (first_msg.count('This'))
print (first_msg.find('variable'))

second_msg = first_msg.replace('first', 'second')

print(second_msg)

greeting = 'Nice to meet you'
name = 'jyson'

msg1 = greeting + ', ' + name
msg2 = greeting + ', ' + name + ' Welcome!'
msg3 = 'msg3 var = {}, {}. Welcome!'.format(greeting, name)
msg4 = f'msg4 var = {greeting}, {name}. Welcome!'
msg5 = f'msg4 var = {greeting}, {name.upper()}. Welcome!'

print(msg1)
print(msg2)
print(msg3)
print(msg4)
print(msg5)
print(help(name))
print(dir(name))