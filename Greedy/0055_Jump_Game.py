"""
LeetCode 55 - Jump Game

Difficulty: Medium

Topics:
- Greedy
- Array

Time Complexity: O(n)

The array is traversed only once.

Space Complexity: O(1)

Only the farthest reachable index is stored.

=============================================================
Explanation
=============================================================

The important idea is to keep track of the farthest
position we can reach so far.

Instead of actually making jumps, we ask:

    "How far can I reach from all positions
     that are currently reachable?"

-------------------------------------------------------------

maxJump = 0

Stores the farthest index we can reach at any point.

Initially we are at index 0, so we can reach at least
index 0.

-------------------------------------------------------------

for i in range(len(nums))

Traverse the array from left to right.

-------------------------------------------------------------

if maxJump < i:

If the farthest position we can reach is before i,
then index i is unreachable.

Since we cannot even reach this position, we can never
reach the end.

Therefore:

return False

-------------------------------------------------------------

maxJump = max(maxJump, nums[i] + i)

If index i is reachable, calculate how far we can reach
from it.

nums[i] is the maximum jump length.

Therefore:

    i + nums[i]

is the farthest position reachable from i.

We compare it with our previous maxJump and keep
the larger value.

-------------------------------------------------------------

if maxJump >= len(nums) - 1:

If the farthest reachable position has reached or
passed the last index, we are done.

Return True.

=============================================================
Dry Run

Example 1

nums = [2,3,1,1,4]

-------------------------------------------------------------

i = 0

maxJump = 0

0 is reachable.

From index 0:

0 + nums[0]

= 0 + 2

= 2

maxJump = 2

-------------------------------------------------------------

i = 1

1 <= 2

Index 1 is reachable.

From index 1:

1 + 3 = 4

maxJump = 4

Last index = 4

maxJump >= 4

Return True.

=============================================================
Example 2

nums = [3,2,1,0,4]

-------------------------------------------------------------

i = 0

maxJump = 3

-------------------------------------------------------------

i = 1

From index 1:

1 + 2 = 3

maxJump remains 3.

-------------------------------------------------------------

i = 2

2 + 1 = 3

maxJump remains 3.

-------------------------------------------------------------

i = 3

3 + 0 = 3

maxJump remains 3.

-------------------------------------------------------------

i = 4

maxJump = 3

But

maxJump < i

3 < 4

Index 4 cannot be reached.

Return False.

=============================================================
Why Greedy Works

We don't care exactly which jumps we make.

We only care about the farthest position that is
reachable so far.

If we can reach index i, then nums[i] gives us
another possible range.

So we continuously expand:

    maxJump = maximum reachable index

If at any point i becomes greater than maxJump,
there is a gap that we cannot cross.

=============================================================
Algorithm

1. Start with maxJump = 0.
2. Traverse every index.
3. If the current index is beyond maxJump,
   return False.
4. Update maxJump using i + nums[i].
5. If maxJump reaches the last index,
   return True.
6. Return False if the loop finishes without reaching it.
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump = 0

        for i in range(len(nums)):

            if maxJump < i:
                return False

            maxJump = max(maxJump, nums[i] + i)

            if maxJump >= len(nums) - 1:
                return True

        return False