## Question
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have `n` versions `[1, 2, ..., n]`and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API `bool isBadVersion(version)` which returns whether `version` is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

#### Example 1:

> Input: n = 5, bad = 4
Output: 4

#### Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.


#### Constraints:

- `1 <= bad <= n <= 231 - 1`

____


## 풀이

최신 버전은 마지막 버전을 베이스로 하여 개발한다. 그래서 나쁜 버전을 베이스로 하면 나쁜 버전의 제품이 만들어진다. `isBadVersion(version)`라는 API가 주어질 때, 가장 처음의 bad version을 찾아야한다.




binary search를 사용하여 첫번째 bad version을 찾았다. 

1. mid 버전이 bad이고 그 앞의 버전이 bad가 아니면 mid버전이 첫번째 bad 버전이다.
2. mid 버전이 bad이고 그 앞의 버전도 bad라면 더이상 뒤에는 볼 필요 없기때문에 high를 mid-1로 바꿔준다. (메모엔 mid라고 되어있다.. 사실 mid로 해도 답은 맞지만 조금이라도 더 빠른 속도를 위해 mid-1로 해주자..)
3. mid 버전이 bad가 아니라면 그 앞에 버전들은 모두 볼 필요 없기때문에 low를 mid+1로 바꿔준다.


-> 이를 반복하여 first bad version을 찾아준다. 


