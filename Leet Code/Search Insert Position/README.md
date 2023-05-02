## Question
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

#### Example 1:


>Input: nums = [1,3,5,6], target = 5
Output: 2


#### Example 2:

> Input: nums = [1,3,5,6], target = 2
Output: 1

#### Example 3:

> Input: nums = [1,3,5,6], target = 7
Output: 4
 

#### Constraints:

- `1 <= nums.length <= 104`
- `-104 <= nums[i] <= 104`
- `nums` contains distinct values sorted in ascending order.
- `-10^4 <= target <= 10^4`


___

## 풀이

```python

class Solution(object):
    def BS(self, nums, low, high, target):
        if high - low < 2:
            return low + 1

        mid = (low + high) // 2
        if nums[mid] >= target:
            return self.BS(nums, low, mid, target)
        else:
            return self.BS(nums, mid, high, target)


    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if nums[0] >= target : 
            return 0
        elif nums[-1] < target:
            return len(nums)
        else:
            low = 0
            high = len(nums)-1
            return self.BS(nums, low, high, target)
```
이 문제는 정렬된 정수 배열과 target이 주어졌을 때, target이 들어갈 자리의 인덱스를 return하는 문제다.

![](https://velog.velcdn.com/images/kimhayeon00/post/54dbbe83-db1e-4194-a9b3-65f911c3e80b/image.JPG)
마음이 급했나보다.. 암튼

런타임이 O(logn)으로 정해져 있어서 binary search를 활용했다.

1. 먼저 가장 첫번째 숫자보다 target이 작으면 0을,
2. 가장 마지막 숫자보다 target이 크면 배열의 크기를 return해줬다.
4. 그리고 BS함수에서 nums[mid]가 target보다 작으면 low를 mid+1로, 그렇지 않으면 high를 mid-1로 바꿔주며 이를 반복해주었다.
4. 나는 범위를 줄여나가며 high-low가 2보다 작을 때, low+1을 return하며 종료해주었다. 


## 개선

내 코드는 target이 들어갈 자리를 찾았어도 모든 low와 high가 만나기 전까진 끝나지 않는다. 
종료되는 조건을 추가해서 효율을 높여볼 수 있을 것 같다.

1. 만약 nums[mid]이 target보다 크거나 같을 때, nums[mid-1]이 target보다 작다면 mid가 insert position이 된다.
2. 만약 nums[mid]이 target보다 작을 때, num[mid+1]이 target보다 크거나 같으면 mid번째 다음이 insert position이다.


다음은 수정된 코드다.

```python

class Solution(object):

    def BS(self, nums, low, high, target):
        mid = (low + high) // 2
        if nums[mid] >= target:
            if nums[mid-1] < target:
                return mid
            return self.BS(nums, low, mid, target)
        else:
            if nums[mid+1] >= target:
                return mid+1
            return self.BS(nums, mid, high, target)

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if nums[0] >= target : 
            return 0
        elif nums[-1] < target:
            return len(nums)
        else:
            low = 0
            high = len(nums)-1
            return self.BS(nums, low, high, target)

```


결과적으로 leetcode에서 제출한 결과 runtime은 38ms -> 34ms, memory는 14.4mb -> 14.1mb로 개선되었다!!



