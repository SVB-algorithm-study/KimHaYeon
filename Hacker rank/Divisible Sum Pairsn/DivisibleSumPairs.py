def divisibleSumPairs(n, k, ar):
    answer = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if (ar[i] + ar[j]) % k == 0:
                 answer += 1
    return answer
