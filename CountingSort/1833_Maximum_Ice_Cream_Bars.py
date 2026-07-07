"""
LeetCode 1833 - Maximum Ice Cream Bars

Difficulty: Medium

Topics:
- Counting Sort
- Greedy
- Array

Time Complexity: O(n + m)
where n = len(costs)
      m = 100000 (maximum possible cost)

Space Complexity: O(m)

=============================================================
Explanation
=============================================================

Instead of sorting the costs array, we use Counting Sort.

The constraints tell us that every cost is between
1 and 100000, so we create a frequency array.

-------------------------------------------------------------

freq = [0] * 100001

freq[i] stores how many ice cream bars have cost i.

Example:

costs = [1,3,2,4,1]

Frequency array:

freq[1] = 2
freq[2] = 1
freq[3] = 1
freq[4] = 1

-------------------------------------------------------------

for cost in costs:
    freq[cost] += 1

Count the occurrence of every price.

-------------------------------------------------------------

for price in range(1, len(freq)):

Traverse prices from the cheapest to the most expensive.

Since we always buy cheaper ice creams first to maximize
the total number purchased, there is no need to sort.

-------------------------------------------------------------

if coins < price:
    continue

If we cannot afford even one ice cream of this price,
move to the next price.

-------------------------------------------------------------

can_buy = min(freq[price], coins // price)

freq[price] tells us how many ice creams are available.

coins // price tells us the maximum number we can afford.

We buy the minimum of these two values.

Example:

price = 3

Available = 5
Coins = 11

coins // 3 = 3

We can buy only

min(5,3) = 3 ice creams.

-------------------------------------------------------------

coins -= can_buy * price

Subtract the total amount spent.

-------------------------------------------------------------

answer += can_buy

Increase the total number of ice creams purchased.

-------------------------------------------------------------

if coins == 0:
    break

Once all coins are spent, no further purchases are possible.

=============================================================

Algorithm

1. Count the frequency of every ice cream price.
2. Traverse prices from lowest to highest.
3. Buy as many ice creams as possible at each price.
4. Reduce the remaining coins.
5. Stop once no coins remain.
6. Return the total number of ice creams purchased.
"""

from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        freq = [0] * 100001

        for cost in costs:
            freq[cost] += 1

        answer = 0

        for price in range(1, len(freq)):
            if coins < price:
                continue

            can_buy = min(freq[price], coins // price)

            answer += can_buy
            coins -= can_buy * price

            if coins == 0:
                break

        return answer