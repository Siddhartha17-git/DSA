"""
LeetCode 231 - Power of Two
LeetCode 342 - Power of Four

Difficulty:
231 - Easy
342 - Easy

Topics:
- Recursion
- Math

Time Complexity:
Power of Two  : O(log₂ n)
Power of Four : O(log₄ n)

Space Complexity:
O(log n) (Recursive Call Stack)

=============================================================
Common Intuition
=============================================================

Both problems repeatedly divide the given number until
it becomes 1.

If at any point the number cannot be divided by the
required base, then it is not a valid power.

Power of Two

2 → 1

4 → 2 → 1

8 → 4 → 2 → 1

16 → 8 → 4 → 2 → 1

-------------------------------------------------------------

Power of Four

4 → 1

16 → 4 → 1

64 → 16 → 4 → 1

256 → 64 → 16 → 4 → 1

=============================================================
Power of Two
=============================================================

Base Cases

If n <= 0

Negative numbers and zero cannot be powers of two.

Return False.

-------------------------------------------------------------

If n == 1

1 = 2⁰

Return True.

-------------------------------------------------------------

If n % 2 != 0

Odd numbers cannot be divided completely by 2.

Return False.

-------------------------------------------------------------

Otherwise

Recursively check

n // 2

until reaching 1.

=============================================================
Power of Four
=============================================================

Base Cases

If n <= 0

Return False.

-------------------------------------------------------------

If n == 1

1 = 4⁰

Return True.

-------------------------------------------------------------

If n % 4 != 0

The number is not divisible by 4.

Return False.

-------------------------------------------------------------

Otherwise

Recursively check

n // 4

until reaching 1.

=============================================================
Algorithm
=============================================================

Power of Two

1. If n <= 0 return False.
2. If n == 1 return True.
3. If n is not divisible by 2 return False.
4. Recursively check n // 2.

-------------------------------------------------------------

Power of Four

1. If n <= 0 return False.
2. If n == 1 return True.
3. If n is not divisible by 4 return False.
4. Recursively check n // 4.
"""

# ----------------------------
# LeetCode 231
# ----------------------------

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 2 != 0:
            return False
        return self.isPowerOfTwo(n // 2)


# ----------------------------
# LeetCode 342
# ----------------------------

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 4 != 0:
            return False
        return self.isPowerOfFour(n // 4)