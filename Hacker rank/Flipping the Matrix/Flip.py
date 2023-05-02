def flippingMatrix(matrix):
    sum = 0
    lm = len(matrix)
    quad = lm//2
    for i in range(quad):
        for j in range(quad):
            p1 = matrix[i][j]
            p2 = matrix[i][lm-j-1]
            p3 = matrix[lm-i-1][j]
            p4 = matrix[lm-i-1][lm-j-1]
            sum += max(p1, p2, p3, p4)
    return sum
