"""
LeetCode 3876 - Construct Uniform Parity Array II

Difficulty: Medium

Topics:
- Math
- Parity
- Array

Time Complexity: O(n)

We find the minimum element and then scan the array
only when necessary.

Space Complexity: O(1)

Only a few variables are used.

=============================================================
Key Observation
=============================================================

We only care about whether numbers are odd or even.

There are two possible goals:

1. Make every element odd.
2. Make every element even.

-------------------------------------------------------------
If there is an odd number
-------------------------------------------------------------

Let the smallest number be odd.

For any even number x, we can subtract an odd number y
such that:

    x - y

is odd.

Because:

    even - odd = odd

So every even element can be made odd.

The odd elements can simply remain unchanged.

Therefore, if the minimum element is odd, the answer
is always True.

-------------------------------------------------------------
If the minimum element is even
-------------------------------------------------------------

Since the array contains distinct positive integers,
if the minimum element is even and there is an odd
element, that odd element cannot be changed into an even
number using a valid positive difference with another
element.

Therefore, every element must already be even.

If we find any odd element, return False.

Otherwise, all elements are already even, so return True.

=============================================================
Explanation of the Code
=============================================================

if min(nums1) % 2 == 1:

Check whether the smallest element is odd.

If it is odd, return True immediately.

-------------------------------------------------------------

else:

The smallest element is even.

Now check whether any element is odd.

-------------------------------------------------------------

for i in nums1:

Traverse every element.

-------------------------------------------------------------

if i % 2 == 1:

An odd element exists while the minimum is even.

Therefore, a uniform parity array cannot be constructed.

Return False.

-------------------------------------------------------------

If the loop finishes,

every element is even.

The original array is already uniformly even.

Return True.

=============================================================
Dry Run 1

nums1 = [1,4,7]

Minimum = 1

1 % 2 = 1

Minimum is odd.

Therefore:

return True

=============================================================
Dry Run 2

nums1 = [2,3]

Minimum = 2

2 is even.

Now check the array:

2 -> even

3 -> odd

An odd element exists.

Therefore:

return False

=============================================================
Dry Run 3

nums1 = [4,6]

Minimum = 4

4 is even.

Check all elements:

4 -> even
6 -> even

No odd elements exist.

Therefore the array is already uniformly even.

return True

=============================================================
Algorithm

1. Find the minimum element.
2. If the minimum is odd, return True.
3. Otherwise, scan the array.
4. If any odd element exists, return False.
5. If all elements are even, return True.
"""

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:

        if min(nums1) % 2 == 1:
            return True

        else:
            for i in nums1:
                if i % 2 == 1:
                    return False

            return True