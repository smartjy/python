#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    # odd, even
    if n % 2 == 0:
        # 2 to 5 and greater than 20
        # if range(2, 5):
        if n >= 2 and n <= 5:
            print('Not Weird')
        # elif range(6, 20):
        elif n >= 6 and n <= 20:
            print('Weird')
        else:
            print('Not Weird')
    else:
        print('Weird')

