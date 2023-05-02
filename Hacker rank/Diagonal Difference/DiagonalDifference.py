
def diagonalDifference(arr):
    # Write your code here
    la = len(arr)
    a = 0
    b = 0
    for i in range(la):
        a += arr[i][i]
        b += arr[i][la-1-i]
    return abs(a-b)
