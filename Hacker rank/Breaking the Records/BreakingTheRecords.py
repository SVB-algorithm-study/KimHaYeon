#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
# this is my code :)
    result = [0, 0]
    best = scores[0]
    worst = scores[0]
    
    for i in range(len(scores)):
        if scores[i] < worst:
            worst = scores[i]
            result[1] += 1
        elif scores[i] > best:
            best = scores[i]
            result[0] += 1
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


