#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    arr_len = len(arr)
    ze = 0
    pl = 0
    mi = 0
    result = []
    for i in arr:
        if i > 0:
            pl = pl + 1
        elif i < 0:
            mi = mi + 1
        elif i == 0:
            ze = ze + 1

    print('%.6f' % (pl / len(arr)))
    print('%.6f' % (mi / len(arr)))
    print('%.6f' % (ze/len(arr)))





        # if arr[i] < 0:
        #     minus = minus + 1
        #     print(sum(minus))


        # elif arr[i] > 0:
        #     print(arr[i])
        # elif arr[i] < 0:
        #     print(arr[i])

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
