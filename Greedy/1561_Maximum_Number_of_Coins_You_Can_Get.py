"""
LeetCode 1561 - Maximum Number of Coins You Can Get

Difficulty: Medium

Topics:
- Greedy
- Sorting

Time Complexity: O(n log n)

Sorting dominates the running time.

Space Complexity: O(1)

(Excluding Python's sorting space.)

=============================================================
Explanation
=============================================================

There are three players:

Alice -> Takes the largest pile.

You -> Take the second largest pile.

Bob -> Takes the smallest pile.

To maximize your coins,

we should make Bob take the smallest piles and Alice
take the largest piles, leaving the second largest
pile for ourselves.

-------------------------------------------------------------

piles.sort(reverse=True)

Sort the piles in descending order.

Example

[2,4,1,2,7,8]

becomes

[8,7,4,2,2,1]

-------------------------------------------------------------

Observation

After sorting,

Alice always gets

8, 4, ...

You should get

7, 2, ...

Bob gets

1, 2, ...

Thus, your piles are every second element among the
largest remaining piles.

-------------------------------------------------------------

for i in range(1, len(piles), 2)

Start from index 1 because

Index 0 -> Alice

Index 1 -> You

Index 2 -> Reserved for Bob later

Index 3 -> Alice

Index 4 -> You

and so on.

-------------------------------------------------------------

ans += piles[i]

Add your selected pile.

-------------------------------------------------------------

if (i + 1) // 2 == len(piles) // 3:
    break

There are exactly n groups where

3n = total piles.

Stop after collecting your n piles.

=============================================================
Dry Run

Example

piles = [2,4,1,2,7,8]

After sorting

[8,7,4,2,2,1]

Alice : 8

You   : 7

Bob   : 1

------------------------

Remaining

[4,2,2]

Alice : 4

You   : 2

Bob   : 2

------------------------

Your total

7 + 2 = 9

=============================================================
Algorithm

1. Sort the piles in descending order.
2. Alice always takes the largest pile.
3. Take every second pile.
4. Repeat until you have collected n piles.
5. Return the total coins.
"""

from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)

        ans = 0

        for i in range(1, len(piles), 2):
            ans += piles[i]

            if (i + 1) // 2 == len(piles) // 3:
                break

        return ans