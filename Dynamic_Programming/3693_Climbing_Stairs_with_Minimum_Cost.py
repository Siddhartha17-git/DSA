"""
LeetCode 3693 - Climbing Stairs with Minimum Cost

Difficulty: Medium

Topics:
- Dynamic Programming

Time Complexity: O(n)

Each step checks only the previous 3 steps.

Space Complexity: O(n)

=============================================================
Explanation
=============================================================

The idea is to find the minimum cost required to reach
every step.

Instead of trying every possible path, we store the
minimum cost to reach each step in a DP array.

-------------------------------------------------------------

dp = [inf] * (n + 1)

dp[i] represents the minimum cost required to reach
step i.

Initially,

dp[0] = 0

because we start from step 0 with no cost.

Every other position is initialized to infinity because
their minimum cost is not known yet.

-------------------------------------------------------------

for i in range(1, n + 1):

Process every step from 1 to n.

For every step, calculate the minimum possible cost to
reach it.

-------------------------------------------------------------

for j in [1, 2, 3]:

A jump can only be of length

1 step
2 steps
3 steps

So we try all three possibilities.

-------------------------------------------------------------

if i - j >= 0:

Ensure the previous step exists.

For example,

If

i = 2

then

2 - 3 = -1

which is an invalid index.

-------------------------------------------------------------

dp[i] = min(
    dp[i],
    dp[i-j] + costs[i-1] + (j * j)
)

Suppose we jump from

(i-j) → i

The total cost becomes

Minimum cost to reach (i-j)

+

Cost of landing on step i

+

Jump cost

The jump cost is

(j²)

because the problem defines

Jump Cost = (distance)²

We calculate this value for all three possible jumps
and keep the minimum.

-------------------------------------------------------------

return dp[n]

dp[n] stores the minimum cost required to reach the
last step.

=============================================================
Dry Run

Example

n = 4

costs = [1,2,3,4]

Initially

dp = [0, inf, inf, inf, inf]

-------------------------------------------------------------

Step 1

Only possible jump

0 → 1

Cost

0 + 1 + 1² = 2

dp = [0,2,inf,inf,inf]

-------------------------------------------------------------

Step 2

From step 1

2 + 2 + 1 = 5

From step 0

0 + 2 + 4 = 6

Choose minimum

dp[2] = 5

-------------------------------------------------------------

Step 3

From step 2

5 + 3 + 1 = 9

From step 1

2 + 3 + 4 = 9

From step 0

0 + 3 + 9 = 12

Choose minimum

dp[3] = 9

-------------------------------------------------------------

Step 4

From step 3

9 + 4 + 1 = 14

From step 2

5 + 4 + 4 = 13

From step 1

2 + 4 + 9 = 15

Choose minimum

dp[4] = 13

Return

13

=============================================================
Algorithm

1. Create a DP array.
2. Set dp[0] = 0.
3. For every step:
      • Try jumping 1 step.
      • Try jumping 2 steps.
      • Try jumping 3 steps.
4. Choose the minimum cost among the three possibilities.
5. Return dp[n].
"""

from typing import List


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for j in [1, 2, 3]:
                if i - j >= 0:
                    dp[i] = min(
                        dp[i],
                        dp[i - j] + costs[i - 1] + (j * j)
                    )

        return dp[n]