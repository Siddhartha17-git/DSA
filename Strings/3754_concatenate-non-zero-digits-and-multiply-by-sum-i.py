"""
LeetCode 3754 - Sum and Multiply

Difficulty: Easy

Topics:
- String

Time Complexity: O(d)
where d is the number of digits in n.

Space Complexity: O(1)

=============================================================
Explanation
=============================================================

The idea is to form a new number using only the non-zero
digits while simultaneously calculating their sum.

-------------------------------------------------------------

x = 0
xsum = 0

x    -> Stores the new number formed using all non-zero
        digits.

xsum -> Stores the sum of all non-zero digits.

-------------------------------------------------------------

for i in str(n):

Convert the integer into a string so that each digit can
be processed one by one.

Example:

n = 10203004

Digits visited:

'1' → '0' → '2' → '0' → '3' → '0' → '0' → '4'

-------------------------------------------------------------

if i != "0":

Ignore every zero because the problem states that only
non-zero digits should be used to form the new number.

-------------------------------------------------------------

digit = int(i)

Convert the current character into an integer.

-------------------------------------------------------------

xsum += digit

Keep adding every non-zero digit.

Example:

Digits = 1, 2, 3, 4

xsum:

0 → 1 → 3 → 6 → 10

-------------------------------------------------------------

x = x * 10 + digit

Append the current digit to the end of x.

Example:

Initially

x = 0

Read 1

x = 1

Read 2

x = 12

Read 3

x = 123

Read 4

x = 1234

-------------------------------------------------------------

return x * xsum

Multiply the newly formed number by the sum of its digits.

Example:

x = 1234

xsum = 10

Answer = 1234 × 10 = 12340

=============================================================

Algorithm

1. Traverse every digit of the number.
2. Skip every zero digit.
3. Build the new number using non-zero digits.
4. Calculate the sum of those digits.
5. Return x × xsum.
"""

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        xsum = 0

        for i in str(n):
            if i != "0":
                digit = int(i)
                xsum += digit
                x = x * 10 + digit

        return x * xsum