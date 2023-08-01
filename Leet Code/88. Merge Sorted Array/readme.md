## Problem
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Constraints:

- nums1.length == m + n
- nums2.length == n
- 0 <= m, n <= 200
- 1 <= m + n <= 200
- -109 <= nums1[i], nums2[j] <= 109
_____
Time Complexity:

The for loop iterates over the nums2 list, which has n elements. Therefore, the loop will run n times.
Inside the loop, assigning the values of nums2 to nums1 takes constant time O(1) for each iteration.
After the loop, the nums1 list is sorted using the built-in sort() method, which has a time complexity of O(m log m).
Combining these steps, the overall time complexity of the merge method is dominated by the sorting step, so it becomes O(m log m), where m is the size of nums1.

Space Complexity:

The space complexity of the merge method is mainly determined by any additional space used by the algorithm, excluding the input and output.
The algorithm doesn't use any additional data structures or arrays apart from the input nums1 and nums2.
Since the sorting operation is performed in-place, it doesn't require any additional space.
Thus, the space complexity of the merge method is O(1), indicating that it uses a constant amount of extra space.

