
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    c = s[8:10] # criteria
    h = s[0:2]  # hour
    e = s[2:8]  # etc

    if c == "PM": # 오후는 12 미만일때만 12 더하기
        if int(h) < 12:
            h = int(h) + 12
    else: # 오전은 12만 0으로 바꾸기
        if int(h) == 12:
            h = 0
    answer = str(h) + e
    if len(answer) < 8:
        answer = '0' + answer
    return answer
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

