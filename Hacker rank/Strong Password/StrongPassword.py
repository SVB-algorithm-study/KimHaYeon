#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    lst = [0,0,0,0]
    for i in password:
        if i in numbers:
            lst[0] += 1
        elif i in lower_case:
            lst[1] += 1
        elif i in upper_case:
            lst[2] += 1
        elif i in special_characters:
            lst[3] += 1
    if sum(lst) >= 6 and 0 not in lst:
        return 0
    else:
        if len(password) + lst.count(0) >= 6:
            return lst.count(0) 
        else:
            return 6 - len(password) 
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
