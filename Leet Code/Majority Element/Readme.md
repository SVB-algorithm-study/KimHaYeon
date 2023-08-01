### Problem
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 
>
Example 1:
Input: nums = [3,2,3]
Output: 3

> Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

### Constraints

- n == nums.length
- 1 <= n <= 5 * 104
- -109 <= nums[i] <= 109
 

**Follow-up: Could you solve the problem in linear time and in O(1) space?**

___

  #### Time Complexity

The code uses a dictionary (dic) to count the occurrences of each element in the nums list.
The loop iterates through each element in the nums list and performs constant time operations (dictionary insertion, addition, and comparison).
In the worst case scenario, where all elements are unique, the loop iterates n times.
Therefore, the time complexity of the code is O(n).


#### Space Complexity

The code uses a dictionary (dic) to store the count of occurrences of each element.
In the worst case scenario, where all elements are unique, the dictionary will have n unique elements, resulting in O(n) space.
Additionally, there is a single integer variable (l) used, which takes constant space.
Therefore, the space complexity of the code is O(n).


___


### Optimization
The code can be optimized to achieve better time complexity by using Boyer-Moore Majority Vote algorithm. This algorithm finds the majority element in O(n) time and O(1) space complexity.
The optimized code only needs a constant amount of space (two variables count and candidate) to find the majority element. The time complexity remains O(n), but the space complexity is reduced to O(1), which is more efficient.
