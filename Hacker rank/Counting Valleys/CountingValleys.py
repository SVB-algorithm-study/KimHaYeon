
def countingValleys(steps, path):
    # Write your code here
    v = 0 #to check valley
    answer = 0
    for i in range(steps):
        if path[i] == 'U':
            v += 1
            if v == 0: # if v turns - to 0
                answer += 1
        else:
            v -= 1
    return answer           
