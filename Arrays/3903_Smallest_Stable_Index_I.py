"""
LeetCode 3903 - Smallest Stable Index I

Difficulty: Easy

Topics:
- Arrays
- Prefix Maximum
- Suffix Minimum

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
We need to find the smallest index i such that:

    max(nums[0..i]) - min(nums[i..n-1]) <= k

To efficiently calculate the minimum value from index i to the end,
we first build a suffix minimum array.

suf[i] stores the minimum element in nums[i..n-1].

Then we scan the array from left to right while maintaining `maxi`,
which stores the maximum value from nums[0..i].

For every index i:
    maxi = max(maxi, nums[i])

The instability score is then:

    maxi - suf[i]

If this value is <= k, i is stable, and since we scan from left
to right, it is automatically the smallest stable index.

If no index satisfies the condition, return -1.


Dry Run:
nums = [5, 0, 1, 4], k = 3

Suffix minimum array:
suf = [0, 0, 1, 4]

Scan from left to right:

i = 0:
    maxi = 5
    score = 5 - 0 = 5
    5 > 3 -> not stable

i = 1:
    maxi = 5
    score = 5 - 0 = 5
    5 > 3 -> not stable

i = 2:
    maxi = 5
    score = 5 - 1 = 4
    4 > 3 -> not stable

i = 3:
    maxi = 5
    score = 5 - 4 = 1
    1 <= 3 -> stable

Return 3.


Algorithm:
1. Create a suffix minimum array `suf`.
2. Set `suf[-1] = nums[-1]`.
3. Traverse from right to left and calculate each suffix minimum.
4. Initialize `maxi = 0`.
5. Traverse nums from left to right.
6. Update `maxi` with the current maximum.
7. Check whether `maxi - suf[i] <= k`.
8. Return i immediately if the condition is satisfied.
9. Return -1 if no stable index exists.
"""

class Solution:

    def firstStableIndex(self, nums: list[int], k: int) -> int:

        n = len(nums)

        suf = [0] * n
        suf[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            suf[i] = min(suf[i + 1], nums[i])

        maxi = 0

        for i in range(n):
            maxi = max(maxi, nums[i])

            if maxi - suf[i] <= k:
                return i

        return -1