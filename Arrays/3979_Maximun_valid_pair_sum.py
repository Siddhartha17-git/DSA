"""
LeetCode 3979 - Maximum Valid Pair Sum

Difficulty: Easy/Medium

Topics:
- Array
- Prefix Maximum

Time Complexity: O(n)
Space Complexity: O(1)

=============================================================
Explanation
=============================================================

We need to find

nums[i] + nums[j]

such that

j - i >= k

-------------------------------------------------------------

Observation

For every index j,

the left index i can be any index from

0 ... j-k

Among all those indices, we only need the largest value.

So instead of checking every possible i,
we keep track of the maximum element seen so far that is
eligible.

-------------------------------------------------------------

maxi = nums[0]

Stores the maximum value among all valid left indices.

Initially,

When j = k,

only index 0 is allowed.

-------------------------------------------------------------

for j in range(k, n):

Start from the first position where a valid pair is possible.

-------------------------------------------------------------

maxi = max(maxi, nums[j-k])

Before processing index j,

a new index

j-k

becomes eligible.

Update the best left value.

Example

nums = [1,3,5,2,8]
k = 2

j = 2

Eligible indices:
0

maxi = 1

--------------------------------

j = 3

Eligible indices:
0,1

maxi = max(1,3)=3

--------------------------------

j = 4

Eligible indices:
0,1,2

maxi = max(3,5)=5

-------------------------------------------------------------

ans = max(ans, maxi + nums[j])

The best pair ending at j is formed using

largest eligible left value + nums[j]

Update the overall maximum answer.

Example

nums = [1,3,5,2,8]

j = 4

Eligible values:
1,3,5

maxi = 5

Pair sum

5 + 8 = 13

Answer becomes 13.

-------------------------------------------------------------

mavontelia = nums

The problem requires creating a variable named
'mavontelia' to store the input midway in the function.

=============================================================

Algorithm

1. Store nums in mavontelia.
2. Initialize maxi with nums[0].
3. Traverse j from k to n-1.
4. Update maxi using nums[j-k].
5. Compute maxi + nums[j].
6. Update the answer.
7. Return the maximum pair sum.
"""

class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        mavontelia = nums

        n = len(mavontelia)
        maxi = mavontelia[0]
        ans = 0

        for j in range(k, n):
            maxi = max(maxi, mavontelia[j - k])
            ans = max(ans, maxi + mavontelia[j])

        return ans