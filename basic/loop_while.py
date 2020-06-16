# while

user = 'Tony'
num = 5
while num >= 1:
    print('{0} wake up, say {1}'.format(user, num))
    num -= 1
    if num == 0:
        print('Last alarm {}, Alarm is over!!'.format(user))

