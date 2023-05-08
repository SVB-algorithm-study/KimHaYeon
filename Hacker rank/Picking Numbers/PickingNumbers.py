

def pickingNumbers(a):
    # Write your code here
    answer = 0
    a = sorted(a)
    # [1, 3, 3, 4, 5, 6]
    for i in range(len(a)-1): # fix one element
        arr = [a[i]] # to save subarray
        for j in range(i+1, len(a)):
            if a[j] - a[i] <= 1: # defference is less than or equal to 1
                arr.append(a[j])
        answer = max(answer, len(arr))
        # print(arr)
        arr = [] # initialize arr
    return answer
                
