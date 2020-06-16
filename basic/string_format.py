URL = 'http://naver.com'

# print(URL)
# a = URL[7:]
a = URL.replace('http://', '')
print('a var: ', a)
# b = a.split('.')
b = a[:a.index('.')]
print('b var: ', b)
c = b[:3] + str(len(b)) + str(b.count('e')) + 'i'
print(c)
print('password = {}, url = {} '.format(URL, c))

# print(c[:3], len(c), c.count('e'), '!')
# print(c[:3] + len(c) + c.count('e'))
