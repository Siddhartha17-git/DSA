"""
LeetCode 3756 - Sum and Multiply

Difficulty: Medium

Topics:
- Array
- Prefix Sum
- Prefix Processing

Time Complexity: O(n + q)

n = length of string
q = number of queries

Space Complexity: O(n)

=============================================================
Explanation
=============================================================

Instead of processing every substring separately, we preprocess
the string once using prefix arrays. This allows every query to
be answered in O(1).

-------------------------------------------------------------

prefSum

prefSum[i] stores the sum of digits from index 0 to i-1.

Example

s = "10203004"

prefSum

Index : 0 1 2 3 4 5 6 7 8

Value : 0 1 1 3 3 6 6 6 10

The sum of digits in any substring [l, r] is

prefSum[r + 1] - prefSum[l]

-------------------------------------------------------------

prefCnt

prefCnt[i] stores the number of non-zero digits seen up to
index i-1.

Example

s = "10203004"

Non-zero digits

1 2 3 4

prefCnt

0 1 1 2 2 3 3 3 4

For every query,

length = prefCnt[r + 1] - prefCnt[l]

This tells us how many digits will be present in x.

-------------------------------------------------------------

prefVal

prefVal stores the number formed using only the non-zero digits.

Whenever the digit is non-zero,

prefVal[i + 1] = prefVal[i] * 10 + digit

If the digit is zero,

prefVal[i + 1] = prefVal[i]

Everything is stored modulo 1e9+7 because the number can
become very large.

Example

s = "10203004"

After processing,

1

12

123

1234

-------------------------------------------------------------

power

power[i] stores

10^i mod (1e9+7)

This helps us remove the contribution of the prefix while
processing each query.

-------------------------------------------------------------

Processing Each Query

length = prefCnt[r + 1] - prefCnt[l]

Number of non-zero digits inside the substring.

-------------------------------------------------------------

start = prefVal[l]

Value before the substring.

-------------------------------------------------------------

end = prefVal[r + 1]

Value after processing the substring.

-------------------------------------------------------------

x = (end - start * power[length]) % MOD

start contains all non-zero digits before the substring.

Multiplying by

power[length]

shifts those digits to the left.

Subtracting removes the prefix contribution and leaves only
the number formed by the current substring.

Example

Entire non-zero number

123456

Suppose substring contributes

345

Then

start = 12

end = 12345

length = 3

12 × 1000 = 12000

12345 − 12000 = 345

-------------------------------------------------------------

xsum = prefSum[r + 1] - prefSum[l]

Find the sum of digits inside the substring.

-------------------------------------------------------------

answer = (x * xsum) % MOD

Multiply the formed number with the digit sum.

=============================================================

Algorithm

1. Build prefix sum array.
2. Build prefix count array for non-zero digits.
3. Build prefix value array containing the concatenated
   non-zero digits.
4. Precompute powers of 10 modulo MOD.
5. For every query:
      • Find the digit sum.
      • Find the number of non-zero digits.
      • Remove the prefix contribution from prefVal.
      • Multiply x with the digit sum.
6. Return all answers.
"""

from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        prefSum = [0] * (n + 1)
        prefVal = [0] * (n + 1)
        prefCnt = [0] * (n + 1)
        power = [1] * (n + 1)

        for i in range(1, n + 1):
            power[i] = (power[i - 1] * 10) % MOD

        for i in range(n):
            digit = int(s[i])

            prefSum[i + 1] = prefSum[i] + digit
            prefCnt[i + 1] = prefCnt[i] + (1 if digit != 0 else 0)

            if digit == 0:
                prefVal[i + 1] = prefVal[i]
            else:
                prefVal[i + 1] = (prefVal[i] * 10 + digit) % MOD

        result = []

        for l, r in queries:

            length = prefCnt[r + 1] - prefCnt[l]

            start = prefVal[l]
            end = prefVal[r + 1]

            x = (end - (start * power[length]) % MOD + MOD) % MOD

            xsum = prefSum[r + 1] - prefSum[l]

            result.append((x * xsum) % MOD)

        return result