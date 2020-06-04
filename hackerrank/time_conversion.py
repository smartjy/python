#!/bin/python3

import os
import sys
import time

#
# Complete the timeConversion function below.
#
def timeConversion(s):

    #
    # Write your code here.
    #
    zn = s[-2:]

    if   zn == 'PM' and s[:2] != '12':
        s = str(int(s[:2]) + 12) + s[2:]
    elif zn == 'AM' and s[:2] == '12':
        s = '00' + s[2:]
    print(s[:-2])


if __name__ == '__main__':
    # f = open(os.environ['/Users/jyson/Developments/python/hackerrank/time_conversion.txt'], 'w')

    s = input()

    result = timeConversion(s)

    # f.write(result + '\n')

    # f.close()


# s = input()
# zn = s[-2:]
# if zn == "PM" and s[:2] != "12":
#     s = str(12 + int(s[:2])) + s[2:]
# if zn == "AM" and s[:2] == "12":
#     s = "00" + s[2:]
# print(s[:-2])