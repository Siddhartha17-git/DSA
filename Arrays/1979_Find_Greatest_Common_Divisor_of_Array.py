"""
LeetCode 1979 - Find Greatest Common Divisor of Array

Difficulty: Easy

Topics:
- Array
- GCD (Euclidean Algorithm)

Time Complexity: O(n log n)

Sorting takes O(n log n).

Finding GCD takes O(log(min(a,b))).

Space Complexity: O(1)
(ignoring the sorting implementation)

=============================================================
Explanation
=============================================================

The problem asks us to find the GCD of the smallest
and largest numbers in the array.

Instead of manually finding them, we sort the array.

-------------------------------------------------------------

gcd(x, y)

Implements Euclid's Algorithm.

Repeatedly replace

(x, y)

with

(y, x % y)

until y becomes 0.

The remaining value of x is the GCD.

-------------------------------------------------------------

nums.sort()

Sort the array in ascending order.

After sorting,

Smallest element

nums[0]

Largest element

nums[-1]

-------------------------------------------------------------

mini = nums[0]

Store the smallest number.

-------------------------------------------------------------

maxi = nums[-1]

Store the largest number.

-------------------------------------------------------------

return gcd(maxi, mini)

Compute the greatest common divisor of the
largest and smallest numbers.

=============================================================
Dry Run

Example

nums = [2,5,6,9,10]

After sorting

[2,5,6,9,10]

mini = 2

maxi = 10

gcd(10,2)

10 % 2 = 0

Answer = 2

=============================================================
Algorithm

1. Sort the array.
2. Take the smallest element.
3. Take the largest element.
4. Compute their GCD.
5. Return the answer.
"""

from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:

        def gcd(x, y):
            while y != 0:
                x, y = y, x % y
            return x

        nums.sort()

        mini = nums[0]
        maxi = nums[-1]

        return gcd(maxi, mini)