### problem

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 ### Constraints

- 1 <= nums.length <= 105
- -231 <= nums[i] <= 231 - 1
- 0 <= k <= 105

 #### Time Complexity:
The time complexity is O(n), where n is the length of the input list nums. The time complexity is determined by the list slicing operation nums[:] = nums[k:] + nums[:k], which rotates the list to the right by k steps. The slicing operation copies the elements of the list, and since we iterate through the entire list once, the time complexity is linear with respect to the size of the input list.

#### Space Complexity
The space complexity is O(n). The primary reason for the space complexity is the list slicing operation nums[:] = nums[k:] + nums[:k], which creates a new list to hold the rotated elements. In the worst case, this operation can create a new list of size n, where n is the length of the input list nums. Therefore, the space complexity is linear with respect to the size of the input list.

____
### Optimization

To optimize the code for rotating the list nums to the right by k steps, we can perform the rotation in-place without using extra space for creating a new list. This can be achieved by using a cyclic rotation approach.

The idea is to reverse the entire list first, then reverse the first k elements, and finally reverse the remaining n - k elements. This will effectively rotate the list to the right by k steps in-place.

With this optimization, the function will rotate the list nums to the right by k steps in-place with a time complexity of O(n) and a space complexity of O(1). It avoids creating any new lists, making it more efficient in terms of space. The time complexity remains O(n) due to the list slicing and reversing operations.





