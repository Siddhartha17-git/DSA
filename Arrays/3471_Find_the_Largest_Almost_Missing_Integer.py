"""
LeetCode 3471 - Find the Largest Almost Missing Integer

Difficulty: Easy

Topics:
- Array
- Hash Map

Time Complexity: O(n)

We traverse nums to build the frequency dictionary
and then traverse it again to find the answer.

Space Complexity: O(n)

The dictionary stores the frequency of each number.

=============================================================
Explanation
=============================================================

An integer is "almost missing" if it appears in exactly
one subarray of size k.

The solution uses the frequency of each number and
the position where it occurs.

-------------------------------------------------------------
Step 1: Count Frequencies
-------------------------------------------------------------

dic = defaultdict(int)

Store:

number -> total frequency in nums

Example:

nums = [3,9,2,1,7]

The dictionary becomes:

3 -> 1
9 -> 1
2 -> 1
1 -> 1
7 -> 1

-------------------------------------------------------------

If a number appears more than once, then for the cases
handled by the solution it cannot be the answer except
for the special cases considered below.

-------------------------------------------------------------
Step 2: Special Case k == n
-------------------------------------------------------------

If:

k == n

there is only one subarray of size k.

That subarray is the entire array.

Therefore every number in nums appears in exactly one
subarray.

So the largest number is the answer:

return max(nums)

-------------------------------------------------------------
Step 3: k == 1
-------------------------------------------------------------

When k == 1, every individual element is its own
subarray.

Therefore a number appears in exactly one size-1
subarray exactly when it occurs once in nums.

So if:

dic[nums[i]] == 1

we can consider nums[i].

-------------------------------------------------------------
Step 4: General Case
-------------------------------------------------------------

For:

1 < k < n

A number that occurs exactly once in nums can appear
in exactly one size-k subarray only if it is at an
endpoint of nums.

Why?

If an element is somewhere in the middle, there are
multiple size-k windows that contain that position.

But if the unique element is at index 0 or n-1,
only one size-k window can contain it.

Therefore:

if dic[nums[i]] == 1

and

i == 0 or i == n - 1

then nums[i] can be almost missing.

-------------------------------------------------------------
output = max(output, nums[i])

Keep the largest valid candidate.

=============================================================
Dry Run

Example:

nums = [3,9,2,1,7]

k = 3

Frequencies:

3 -> 1
9 -> 1
2 -> 1
1 -> 1
7 -> 1

-------------------------------------------------------------

3 is at index 0.

It occurs once and is at an endpoint.

Candidate = 3

output = 3

-------------------------------------------------------------

9 is in the middle.

It occurs once but is not at an endpoint.

Ignore it.

-------------------------------------------------------------

2 -> middle

Ignore.

-------------------------------------------------------------

1 -> middle

Ignore.

-------------------------------------------------------------

7 is at index 4.

It occurs once and is at an endpoint.

Candidate = 7

output = 7

Final answer:

7

=============================================================
Algorithm

1. Count the frequency of every number.
2. If k == n, return the maximum element.
3. Traverse nums.
4. If an element occurs exactly once:
   - For k == 1, it is a candidate.
   - Otherwise, it must be at index 0 or n-1.
5. Keep the largest candidate.
6. Return the answer.
"""

from collections import defaultdict
from typing import List


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:

        dic = defaultdict(int)
        output = -1
        n = len(nums)

        for i in nums:
            dic[i] += 1

        for i in range(n):

            if k == n:
                return max(nums)

            if dic[nums[i]] == 1:

                if k == 1:
                    output = max(output, nums[i])

                if i == 0 or i == n - 1:
                    output = max(output, nums[i])

        return output