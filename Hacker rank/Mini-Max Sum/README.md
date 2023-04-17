## Question
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

#### Example
> arr = [1, 3, 5, 7, 9]

The minimum sum is `1 + 3 + 5 + 7 = 16` and the maximum sum is `3 + 5 + 7 + 9 = 24`. The function prints

> 16 24

#### Function Description

Complete the miniMaxSum function in the editor below.

miniMaxSum has the following parameter(s):

- arr: an array of 5 integers
#### Print

Print two space-separated integers on one line: the minimum sum and the maximum sum of 4 of 5 elements.

#### Input Format

A single line of five space-separated integers.

#### Constraints
> 1 <= arr[i] <= 10^9

#### Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

#### Sample Input

> 1 2 3 4 5

#### Sample Output

> 10 14


## 풀이


총 합에서 최댓값을 뺀 값, 총 합에서 최솟값을 뺀 값을 출력해주면 되는 쉬운 문제였다. 

나는 파이썬 내장함수를 사용해서 간단하게 구현했다.

추가로
``` python
print(sum(arr)-max(arr), sum(arr)-min(arr))
```
이렇게 썼지만
``` python
print(sum(arr)-max(arr), end = " ")
print(sum(arr)-min(arr))
```
처음엔 이렇게 썼다. 문제도 안읽고 두 줄로 출력했다가 틀렸기 때문이다.. 문제좀 제대로 읽어보자~!
