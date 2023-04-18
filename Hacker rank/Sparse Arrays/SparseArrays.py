def matchingStrings(strings, queries):
    s = strings
    q = queries
    answer = [0 for i in range(len(q))]
    for i in range(len(q)):
        for j in range(len(s)):
            if q[i] == s[j]:
                answer[i] += 1
        
    return answer
