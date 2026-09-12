"""
LeetCode 238 - Product of Array Except Self

Difficulty: Medium

Topics:
- Arrays
- Prefix Product
- Suffix Product

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
For every index i, we need the product of all elements except nums[i].

We can split this product into two parts:

    product of elements before i
    *
    product of elements after i

To calculate these efficiently, we create two arrays:

1. `pref`
   pref[i] stores the product of nums[0] through nums[i].

2. `rev_pref`
   rev_pref[i] stores the product of nums[i] through nums[n-1].

For an index i:
- If i is the first index, there is no prefix, so we use the
  suffix product starting at i + 1.
- If i is the last index, there is no suffix, so we use the
  prefix product ending at i - 1.
- Otherwise, multiply the prefix product before i by the suffix
  product after i.

This also naturally handles zeroes because we never use division.


Dry Run:
nums = [1, 2, 3, 4]

Prefix products:
pref = [1, 2, 6, 24]

Suffix products:
rev_pref = [24, 24, 12, 4]

Now calculate the answer:

i = 0:
    rev_pref[1] = 24

i = 1:
    pref[0] * rev_pref[2]
    = 1 * 12
    = 12

i = 2:
    pref[1] * rev_pref[3]
    = 2 * 4
    = 8

i = 3:
    pref[2] = 6

Answer:
[24, 12, 8, 6]


Algorithm:
1. Create a prefix product array `pref`.
2. Create a suffix product array `rev_pref`.
3. Build `pref` from left to right.
4. Build `rev_pref` from right to left.
5. For every index:
   - First index -> use suffix product.
   - Last index -> use prefix product.
   - Middle index -> multiply prefix and suffix products.
6. Return the resulting array.
"""

class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        pref = [0] * n
        rev_pref = [0] * n

        pref[0] = nums[0]
        rev_pref[-1] = nums[-1]

        for i in range(1, n):
            pref[i] = nums[i] * pref[i - 1]

        for i in range(n - 2, -1, -1):
            rev_pref[i] = nums[i] * rev_pref[i + 1]

        ans = []

        for i in range(n):
            if i == 0:
                ans.append(rev_pref[i + 1])
            elif i == n - 1:
                ans.append(pref[i - 1])
            else:
                ans.append(pref[i - 1] * rev_pref[i + 1])

        return ans