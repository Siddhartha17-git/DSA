"""
LeetCode 2996 - Smallest Missing Integer Greater Than Sequential Prefix Sum

Difficulty: Easy

Topics:
- Array
- Hash Set

Time Complexity: O(n)

The array is traversed once to find the sequential prefix,
and the set provides O(1) average lookup.

Space Complexity: O(n)

The set stores the elements of nums.

=============================================================
Explanation
=============================================================

The problem has two main steps:

1. Find the sum of the longest sequential prefix.
2. Starting from that sum, find the smallest integer
   that does not exist in nums.

-------------------------------------------------------------
Step 1: Find the Sequential Prefix Sum
-------------------------------------------------------------

The first element always belongs to the sequential prefix.

So we start with:

prefsum = nums[0]

Then we check consecutive elements.

For the prefix to remain sequential:

nums[i] + 1 == nums[i + 1]

must be true.

-------------------------------------------------------------

Example:

nums = [1,2,3,2,5]

Start:

prefsum = 1

-------------------------------------------------------------

1 + 1 == 2

Yes.

prefsum = 1 + 2

= 3

-------------------------------------------------------------

2 + 1 == 3

Yes.

prefsum = 3 + 3

= 6

-------------------------------------------------------------

3 + 1 == 2

False.

The sequential prefix ends here.

So:

prefsum = 6

-------------------------------------------------------------
Step 2: Create a Set
-------------------------------------------------------------

s = set(nums)

We create a set so that we can quickly check whether
a number exists in the array.

For example:

nums = [1,2,3,2,5]

s = {1,2,3,5}

-------------------------------------------------------------
Step 3: Find the Missing Integer
-------------------------------------------------------------

We start checking from prefsum.

If prefsum is already present in the set,
increase it by 1.

Continue until we find a number that is not present.

-------------------------------------------------------------

Example:

prefsum = 6

6 not in set

Therefore:

return 6

-------------------------------------------------------------

Example 2:

nums = [3,4,5,1,12,14,13]

Sequential prefix:

[3,4,5]

Sum:

3 + 4 + 5 = 12

Set contains:

12, 13, 14

So:

12 -> exists
13 -> exists
14 -> exists
15 -> missing

Answer:

15

=============================================================
Algorithm

1. Start the prefix sum with nums[0].
2. Traverse the array while consecutive elements
   increase by exactly 1.
3. Add each sequential element to prefsum.
4. Stop when the sequential prefix ends.
5. Convert nums into a set.
6. Start from prefsum.
7. If the current number exists in the set,
   increment it.
8. Return the first missing number.
"""

from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:

        prefsum = nums[0]

        s = set(nums)

        for i in range(len(nums) - 1):

            if nums[i] + 1 == nums[i + 1]:
                prefsum += nums[i + 1]

            else:
                break

        while True:

            if prefsum not in s:
                return prefsum

            prefsum += 1