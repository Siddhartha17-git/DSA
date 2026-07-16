"""
LeetCode 3658 - GCD of Odd and Even Sums
LeetCode 3867 - GCD Pair Sum

Difficulty:
3658 - Easy
3867 - Medium

Topics:
- Array
- GCD (Euclidean Algorithm)

=============================================================
Common Concept
=============================================================

Both problems use the Euclidean Algorithm to compute
the Greatest Common Divisor (GCD).

Algorithm

While y != 0

    x, y = y, x % y

When y becomes 0,

x is the GCD.

Time Complexity

O(log(min(x, y)))

=============================================================
LeetCode 3658
=============================================================

Idea

Instead of generating the odd and even numbers,
we use mathematical formulas.

-------------------------------------------------------------

sumOdd = n * n

The sum of the first n odd numbers is

1 + 3 + 5 + ...

= n²

-------------------------------------------------------------

sumEven = n * (n + 1)

The sum of the first n even numbers is

2 + 4 + 6 + ...

= n(n+1)

-------------------------------------------------------------

while sumOdd != 0

Apply Euclid's Algorithm.

Example

n = 4

sumOdd = 16

sumEven = 20

20 % 16 = 4

16 % 4 = 0

Answer = 4

=============================================================
LeetCode 3867
=============================================================

Idea

Construct prefixGcd.

Sort it.

Pair the smallest and largest values.

Compute the GCD of every pair.

-------------------------------------------------------------

gcd()

Custom implementation of Euclid's Algorithm.

-------------------------------------------------------------

mx

Stores the maximum element seen so far.

-------------------------------------------------------------

for i in range(n)

Update the running maximum.

mx = max(mx, nums[i])

Compute

gcd(mx, nums[i])

and store it inside prefixGcd.

-------------------------------------------------------------

prefixGcd.sort()

Sort the array so we can pair

Smallest ↔ Largest

Second Smallest ↔ Second Largest

...

-------------------------------------------------------------

i = 0
j = n - 1

Use two pointers.

Example

prefixGcd

[2,3,6,8]

Pairs

(2,8)

(3,6)

-------------------------------------------------------------

gcd(prefixGcd[j], prefixGcd[i])

Compute the GCD of each pair.

-------------------------------------------------------------

tsum += gcdij

Add every pair GCD into the final answer.

Continue until

i >= j

=============================================================
Algorithms
=============================================================

LeetCode 3658

1. Compute sumOdd = n².
2. Compute sumEven = n(n+1).
3. Apply Euclid's Algorithm.
4. Return the GCD.

-------------------------------------------------------------

LeetCode 3867

1. Construct prefixGcd.
2. Sort prefixGcd.
3. Pair smallest and largest elements.
4. Compute the GCD of every pair.
5. Return the total sum.
"""

# ----------------------------------------------------------
# LeetCode 3658
# ----------------------------------------------------------

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = n * n
        sumEven = n * (n + 1)

        while sumOdd != 0:
            div = sumEven // sumOdd
            rem = sumEven % sumOdd

            sumEven = sumOdd
            sumOdd = rem

        return sumEven


# ----------------------------------------------------------
# LeetCode 3867
# ----------------------------------------------------------

class Solution:
    def gcdSum(self, nums: list[int]) -> int:

        def gcd(x, y):
            while y != 0:
                x, y = y, x % y
            return x

        n = len(nums)

        prefixGcd = []

        mx = float("-inf")

        for i in range(n):
            mx = max(mx, nums[i])
            ele = gcd(mx, nums[i])
            prefixGcd.append(ele)

        prefixGcd.sort()

        tsum = 0

        i = 0
        j = n - 1

        while i < j:
            gcdij = gcd(prefixGcd[j], prefixGcd[i])
            tsum += gcdij

            i += 1
            j -= 1

        return tsum