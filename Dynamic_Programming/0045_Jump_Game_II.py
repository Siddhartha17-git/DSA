
"""
LeetCode 45 - Jump Game II

Difficulty: Medium

Topics:
- Greedy
- Dynamic Programming
- Arrays

Solution 1: Dynamic Programming
Time Complexity: O(n^2)
Space Complexity: O(n)

Solution 2: Greedy
Time Complexity: O(n)
Space Complexity: O(1)


PROBLEM SUMMARY:
Each nums[i] tells us the maximum distance we can jump forward.
Find the minimum number of jumps needed to reach the last index.


SOLUTION 1: DYNAMIC PROGRAMMING

Approach:
dp[i] represents the minimum number of jumps needed to reach index i.

Initially:
    dp[0] = 0
    dp[i] = infinity for all other indices

For every destination index i, check all previous indices j.
If j + nums[j] >= i, we can reach i from j.

Therefore:
    dp[i] = min(dp[i], dp[j] + 1)

After checking all possible previous indices, dp[n - 1]
contains the minimum number of jumps.


Dry Run:
nums = [2, 3, 1, 1, 4]

Initial:
dp = [0, inf, inf, inf, inf]

i = 1:
    Reachable from index 0.
    dp[1] = 1

i = 2:
    Reachable from index 0 or 1.
    dp[2] = 1

i = 3:
    Reachable from index 1.
    dp[3] = 2

i = 4:
    Reachable from index 1.
    dp[4] = 2

Answer = 2


SOLUTION 2: GREEDY

Approach:
Instead of calculating the minimum jumps for every index,
we process the array in ranges.

range_min and range_max represent the current range of indices
reachable using the current number of jumps.

For every index in this range, calculate:
    i + nums[i]

This gives the farthest index reachable from that position.

`last` stores the farthest index reachable from the entire
current range.

After processing the range:
    range_min = range_max + 1
    range_max = last

We increment the jump count because we have moved to the next
range of reachable indices.

We repeat until the last index is reachable.


Dry Run:
nums = [2, 3, 1, 1, 4]

Initial:
count = 0
range_min = 0
range_max = 0

First range: [0]
    Index 0 can reach index 2.
    last = 2

    New range = [1, 2]
    count = 1

Second range: [1, 2]
    Index 1 can reach index 4.
    Index 2 can reach index 3.
    last = 4

    New range reaches the last index.
    count = 2

Answer = 2


ALGORITHM SUMMARY:

Dynamic Programming:
1. Initialize dp with infinity and set dp[0] = 0.
2. For each index i, inspect all previous indices j.
3. If j + nums[j] >= i, update dp[i] with dp[j] + 1.
4. Return dp[n - 1].

Greedy:
1. Initialize the jump count and current range boundaries to 0.
2. Find the farthest reachable index from the current range.
3. Move the range boundaries forward.
4. Increment the jump count.
5. Repeat until the last index is reachable.
6. Return the jump count.
"""

from typing import List


class Solution:
    # Solution 1: Dynamic Programming - O(n^2)
    def jump_dp(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [float('inf')] * n
        dp[0] = 0

        for i in range(n):
            for j in range(i):
                if j + nums[j] >= i:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[n - 1]

    # Solution 2: Greedy - O(n)
    def jump(self, nums: List[int]) -> int:
        count = 0
        range_min = 0
        range_max = 0

        while range_max < len(nums) - 1:
            last = 0

            for i in range(range_min, range_max + 1):
                last = max(i + nums[i], last)

            range_min = range_max + 1
            range_max = last
            count += 1

        return count
