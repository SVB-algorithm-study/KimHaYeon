## Question

Given an array of integers and a positive integer `k` , determine the number of `(i,j)` pairs where  and `ar[i]` + `ar[j]` is divisible by `k`.


#### Function Description

Complete the divisibleSumPairs function in the editor below.

divisibleSumPairs has the following parameter(s):

- int n: the length of array 
- int ar[n]: an array of integers
- int k: the integer divisor
#### Returns
- int: the number of pairs

#### Input Format

The first line contains 2 space-separated integers n,  and k.
The second line contains n space-separated integers, each a value of arr[i].

#### Constraints
- 2 <= n <= 100
- 1 <= k <= 100
- 1 <= ar[i] <= 100

#### Sample Input
>
STDIN           Function
-----           --------
6 3             n = 6, k = 3
1 3 2 6 1 2     ar = [1, 3, 2, 6, 1, 2]


#### Sample Output

 > 5
