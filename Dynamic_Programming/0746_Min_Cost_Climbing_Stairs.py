"""
LeetCode 746 - Min Cost Climbing Stairs

Difficulty: Easy

Topics:
- Dynamic Programming
- Arrays

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
We use a DP array where dp[i] represents the minimum cost required
to reach step i.

To reach step i, we can come from either:
    1. Step i - 1
    2. Step i - 2

If we come from step i - 1, we must pay cost[i - 1].
If we come from step i - 2, we must pay cost[i - 2].

Therefore:

    dp[i] = min(
        dp[i - 1] + cost[i - 1],
        dp[i - 2] + cost[i - 2]
    )

The top of the staircase is just after the last index, so we can
reach it either from the last step or the second-last step.

Therefore the final answer is:

    min(
        dp[-1] + cost[-1],
        dp[-2] + cost[-2]
    )


Dry Run:
cost = [10, 15, 20]

Initialize:
dp = [0, 0, 0]

i = 2:
    dp[2] = min(dp[1] + cost[1],
                dp[0] + cost[0])

         = min(0 + 15, 0 + 10)
         = 10

So:
dp = [0, 0, 10]

To reach the top:
    min(dp[-1] + cost[-1],
        dp[-2] + cost[-2])

  = min(10 + 20,
        0 + 15)

  = min(30, 15)
  = 15

Answer = 15.


Algorithm:
1. Create a DP array of size n initialized with 0.
2. Start calculating from index 2.
3. For every index i, calculate the minimum cost to reach it from
   either the previous step or the step before that.
4. After filling the DP array, calculate the cost of reaching the
   top from either of the final two steps.
5. Return the smaller cost.
"""

class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp = [0] * len(cost)

        for i in range(2, len(cost)):
            dp[i] = min(
                dp[i - 1] + cost[i - 1],
                dp[i - 2] + cost[i - 2]
            )

        return min(
            dp[-1] + cost[-1],
            dp[-2] + cost[-2]
        )