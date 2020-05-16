# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Grater or Equal:  >=
# Less or Equal:    <=
# Object Identity   is

language = 'Python'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No Python')

# and
# or
# not

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin page')
else:
    print('Bad Credential')

if not logged_in:
    print('Please Login')
else:
    print('Welcome')

