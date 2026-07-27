"""
LeetCode 1464 - Maximum Product of Two Elements in an Array

Difficulty: Easy

Topics:
- Array

Time Complexity: O(n)

The array is traversed only once.

Space Complexity: O(1)

Only two variables are used to store the largest elements.

=============================================================
Explanation
=============================================================

The idea is to find the largest and second largest
elements in the array without sorting it.

Once these two values are known, the required answer is

(max1 - 1) × (max2 - 1)

-------------------------------------------------------------

max1 = max2 = -1

max1 stores the largest element.

max2 stores the second largest element.

Initially both are -1 because every array element
is greater than or equal to 1.

-------------------------------------------------------------

for i in range(len(nums))

Traverse every element of the array.

-------------------------------------------------------------

if nums[i] >= max1

A new maximum element is found.

The previous maximum becomes the second maximum.

Example

Current

max1 = 7

max2 = 5

New element = 9

After updating

max1 = 9

max2 = 7

-------------------------------------------------------------

elif nums[i] >= max2

The current element is not larger than max1,
but it is larger than the current second maximum.

Update only max2.

Example

Current

max1 = 9

max2 = 5

New element = 8

After updating

max2 = 8

-------------------------------------------------------------

return (max1 - 1) * (max2 - 1)

After finding the two largest numbers,

subtract 1 from each and multiply them.

=============================================================
Dry Run

Example

nums = [3,4,5,2]

Initially

max1 = -1

max2 = -1

----------------

3

max1 = 3

max2 = -1

----------------

4

max1 = 4

max2 = 3

----------------

5

max1 = 5

max2 = 4

----------------

2

No update

----------------

Answer

(5-1) × (4-1)

= 4 × 3

= 12

=============================================================
Algorithm

1. Initialize the largest and second largest values.
2. Traverse the array once.
3. Update the two largest elements whenever required.
4. Compute

   (max1 - 1) × (max2 - 1)

5. Return the result.
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = max2 = -1

        for i in range(len(nums)):
            if nums[i] >= max1:
                max2 = max1
                max1 = nums[i]

            elif nums[i] >= max2:
                max2 = nums[i]

        return (max1 - 1) * (max2 - 1)