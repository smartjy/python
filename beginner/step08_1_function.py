# Function
def hello_func():
    print('Hello Function!')

print('Funtion memory location :', hello_func)
print('Funtion execution :', hello_func())
# hello_func()

print('')

def hello_func1():
    return 'Hello Function return.'

# hello_func1()
print(hello_func1())

print('')

def hello_func2(greeting):
    return '{} Function.'.format(greeting)

print(hello_func2('Hi there'))

print('')

def hello_func3(greeting, name='Programming'):
    return '{}, {}'.format(greeting, name)
print(hello_func3('Hi', name = 'Python'))

print('')

def emplyee_info(*args, **kwargs):
    print(args)
    print(kwargs)
    # print(kwargs)
emplyee_info('Math', 'Art', name='John', age=32)

print('')
def emplyee_info1(*args, **kwargs):
    print(args)
    print(kwargs)
    # print(kwargs)
courses = ['Java', 'Python']
info = {'name': 'Jay', 'age':33}
emplyee_info1(*courses, **info)

