"""
LeetCode 525 - Contiguous Array

Difficulty: Medium

Topics:
- Hash Map
- Prefix Sum
- Array

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
We need to find the longest contiguous subarray containing an equal
number of 0s and 1s.

We treat:
    0 -> -1
    1 -> +1

Now, a subarray has an equal number of 0s and 1s exactly when its
sum is 0.

Instead of actually modifying the array, we maintain a running
prefix sum `k`.

For every index:
    - If nums[i] == 0, decrease k by 1.
    - If nums[i] == 1, increase k by 1.

We use a dictionary `dic` to store the FIRST index at which each
prefix sum occurs.

Why store only the first occurrence?

If the same prefix sum appears again at index i, the subarray between
the first occurrence and i has sum 0. Therefore, it contains an equal
number of 0s and 1s.

The earliest occurrence gives the longest possible subarray ending
at the current index.


Important Initialization:
    dic = {0: -1}

This represents a prefix sum of 0 occurring before the array starts.

For example, if the running sum becomes 0 at index 1:

    length = 1 - (-1) = 2

which correctly represents the subarray nums[0..1].


Dry Run:
nums = [0, 1, 0]

Initial:
    dic = {0: -1}
    k = 0
    ans = 0

i = 0:
    nums[0] = 0
    k = -1

    -1 is not in dic
    dic[-1] = 0

i = 1:
    nums[1] = 1
    k = 0

    0 is already in dic at -1

    length = 1 - (-1) = 2
    ans = 2

i = 2:
    nums[2] = 0
    k = -1

    -1 is already in dic at 0

    length = 2 - 0 = 2
    ans remains 2

Return 2.


Algorithm:
1. Initialize a dictionary with `{0: -1}`.
2. Initialize the running prefix sum `k = 0`.
3. Traverse the array.
4. Treat 0 as -1 and 1 as +1.
5. If the current prefix sum has appeared before:
   - Calculate the length of the subarray.
   - Update the maximum length.
6. Otherwise, store the current index as the FIRST occurrence
   of this prefix sum.
7. Return the maximum length.
"""

class Solution:

    def findMaxLength(self, nums: List[int]) -> int:

        dic = {0: -1}

        k = 0
        ans = 0

        for i in range(len(nums)):

            if nums[i] == 0:
                k -= 1
            else:
                k += 1

            if k in dic:
                ans = max(ans, i - dic[k])
            else:
                dic[k] = i

        return ans