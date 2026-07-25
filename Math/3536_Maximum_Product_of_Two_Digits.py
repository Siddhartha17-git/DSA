"""
LeetCode 3536 - Maximum Product of Two Digits

Difficulty: Easy

Topics:
- Digit Manipulation

Time Complexity: O(d)

where d is the number of digits in n.

Space Complexity: O(1)

=============================================================
Explanation
=============================================================

The idea is to find the largest and second largest
digit while traversing the number only once.

Instead of storing all digits or sorting them,
we maintain only two variables.

-------------------------------------------------------------

maxi1 = -1
maxi2 = -1

maxi1 stores the largest digit seen so far.

maxi2 stores the second largest digit seen so far.

-------------------------------------------------------------

while n > 0

Process every digit from right to left.

Current digit

digit = n % 10

Remove the last digit

n //= 10

Example

n = 5382

Digits visited

2 → 8 → 3 → 5

-------------------------------------------------------------

if digit > maxi1

A new largest digit is found.

The previous largest becomes the second largest.

Example

Current

maxi1 = 6

maxi2 = 4

New digit = 8

After updating

maxi1 = 8

maxi2 = 6

-------------------------------------------------------------

elif digit > maxi2

The digit is not larger than the maximum,
but it is larger than the current second maximum.

Update only maxi2.

Example

Current

maxi1 = 9

maxi2 = 5

New digit = 7

After updating

maxi2 = 7

-------------------------------------------------------------

return maxi1 * maxi2

After processing every digit,

maxi1 and maxi2 are the two largest digits.

Their product is the required answer.

=============================================================
Dry Run

Example

n = 124

Digits visited

4

maxi1 = 4

maxi2 = -1

----------------

2

maxi1 = 4

maxi2 = 2

----------------

1

No update

----------------

Answer

4 × 2 = 8

=============================================================
Algorithm

1. Initialize the two largest digits.
2. Traverse every digit of the number.
3. Update the largest and second largest digit.
4. Return their product.
"""

class Solution:
    def maxProduct(self, n: int) -> int:
        maxi1, maxi2 = -1, -1

        while n > 0:
            digit = n % 10

            if digit > maxi1:
                maxi2 = maxi1
                maxi1 = digit

            elif digit > maxi2:
                maxi2 = digit

            n //= 10

        return maxi1 * maxi2