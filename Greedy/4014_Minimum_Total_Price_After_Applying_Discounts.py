"""
LeetCode 4014 - Minimum Total Price After Applying Discounts

Difficulty: Medium

Topics:
- Greedy
- Sorting

Time Complexity: O(n log n + m log m)

Sorting prices and discounts dominates the complexity.

Space Complexity: O(1)

Ignoring the space used internally by sorting.

=============================================================
Explanation
=============================================================

We want to minimize the final total price.

For an item with price x and discount y:

    final price = x - (x * y / 100)

The amount of money saved is:

    x * y / 100

Therefore, to maximize the total savings, we should
pair the largest prices with the largest discounts.

This gives the greedy strategy:

    Largest price  <-> Largest discount
    2nd largest    <-> 2nd largest
    ...

-------------------------------------------------------------

prices.sort(reverse=True)

Sort prices from largest to smallest.

Example:

prices = [10,30,21]

becomes

[30,21,10]

-------------------------------------------------------------

discounts.sort(reverse=True)

Sort discounts from largest to smallest.

Example:

discounts = [50,60]

becomes

[60,50]

-------------------------------------------------------------

Now pair them in the same order:

30 <-> 60%

21 <-> 50%

This maximizes the total amount saved.

-------------------------------------------------------------

discount(x, y)

Calculates the final price after applying discount y
to price x.

    x - (x * y / 100)

Example:

30 with 60%

30 - (30 * 60 / 100)

= 30 - 18

= 12

-------------------------------------------------------------

for i in range(min(len(prices), len(discounts)))

Apply discounts while both a price and discount
are available.

-------------------------------------------------------------

total += price

Add the discounted price to the total.

-------------------------------------------------------------

for i in range(len(discounts), len(prices))

If there are more prices than discounts, the remaining
items receive no discount.

Therefore, add their original prices.

=============================================================
Dry Run

Example:

prices = [10,30,21]

discounts = [50,60]

-------------------------------------------------------------

Sort prices:

[30,21,10]

Sort discounts:

[60,50]

-------------------------------------------------------------

30 with 60%

30 - 18 = 12

-------------------------------------------------------------

21 with 50%

21 - 10.5 = 10.5

-------------------------------------------------------------

10 has no discount

10

-------------------------------------------------------------

Total:

12 + 10.5 + 10

= 32.5

=============================================================
Why the Greedy Strategy Works

The saving produced by pairing price p with discount d is:

    p * d / 100

Ignoring the constant 1/100, we want to maximize:

    p * d

For two prices:

    p1 > p2

and two discounts:

    d1 > d2

Pairing them as:

    p1*d1 + p2*d2

is at least as good as:

    p1*d2 + p2*d1

because:

    p1*d1 + p2*d2
    - p1*d2 - p2*d1

    = (p1-p2)(d1-d2)

    >= 0

Therefore, pairing both arrays in descending order
maximizes the total discount and minimizes the final price.

=============================================================
Algorithm

1. Sort prices in descending order.
2. Sort discounts in descending order.
3. Pair the largest price with the largest discount.
4. Calculate each discounted price.
5. Add undiscounted prices if there are more prices
   than discounts.
6. Return the total.
"""

class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:

        def discount(x, y):
            price = x - (x * (y / 100))
            return price

        prices.sort(reverse=True)
        discounts.sort(reverse=True)

        total = 0

        for i in range(min(len(prices), len(discounts))):
            price = discount(prices[i], discounts[i])
            total += price

        for i in range(len(discounts), len(prices)):
            total += prices[i]

        return total