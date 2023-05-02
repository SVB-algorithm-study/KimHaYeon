def sockMerchant(n, ar):
    # Write your code here
    set_ar = set(ar)
    answer = 0
    for i in set_ar:
        cnt = ar.count(i)
        if cnt > 1:
            answer += cnt//2
    return answer
