
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
lines = sys.stdin.readlines()
lines = [line.rstrip() for line in lines]
for s in lines:
    word = s[4:]
    tmp = ''
    answer = ''
    #split
    if s[0] == 'S':
        if s[2] == 'M':
            word = word[:-2]
        for i in range(len(word)):
            if word[i].isupper():
                if tmp:
                    answer = answer + tmp + " " 
                    tmp = ''
            tmp += word[i].lower()
        answer += tmp
    #combine
    else:
        lst = word.split()
        answer = lst[0]
        for i in range(1, len(lst)):
            answer += lst[i][0].upper()
            answer += lst[i][1:]
        if s[2] == 'M':
            answer += '()'  
        if s[2] == 'C':
            answer = answer[0].upper() + answer[1:]
    print(answer)
