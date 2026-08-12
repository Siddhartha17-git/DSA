"""
LeetCode 128 - Longest Consecutive Sequence

Difficulty: Medium

Topics:
- Hash Set
- Array

Time Complexity: O(n)

Each number is processed as the start of a sequence
only when its previous number does not exist.

Space Complexity: O(n)

The set stores all elements.

=============================================================
Explanation
=============================================================

The goal is to find the longest sequence of consecutive
integers.

Example:

nums = [100,4,200,1,3,2]

The longest sequence is:

1 -> 2 -> 3 -> 4

Length = 4

-------------------------------------------------------------

s = set(nums)

Convert nums into a set.

This allows us to check whether a number exists in
O(1) average time.

It also automatically removes duplicates.

-------------------------------------------------------------

for i in s:

Traverse every unique number.

-------------------------------------------------------------

if i - 1 not in s:

This is the most important condition.

If i - 1 does not exist, then i is the START of
a consecutive sequence.

Example:

s = {1,2,3,4}

For 1:

0 is not present.

Therefore 1 is a sequence start.

For 2:

1 is present.

Therefore 2 is not a sequence start.

This prevents us from unnecessarily scanning the same
sequence multiple times.

-------------------------------------------------------------

curr = 1

Start the current sequence with length 1.

-------------------------------------------------------------

x = i

x represents the current number in the sequence.

-------------------------------------------------------------

while x + 1 in s:

Check whether the next consecutive number exists.

If it exists:

curr += 1

x += 1

Continue expanding the sequence.

-------------------------------------------------------------

c = max(c, curr)

Keep track of the longest sequence found so far.

=============================================================
Dry Run

nums = [100,4,200,1,3,2]

Set:

{1,2,3,4,100,200}

-------------------------------------------------------------

i = 1

0 not in set.

So 1 is the start of a sequence.

x = 1

1 + 1 = 2 → exists

curr = 2

x = 2

2 + 1 = 3 → exists

curr = 3

x = 3

3 + 1 = 4 → exists

curr = 4

x = 4

5 not in set.

Sequence length = 4.

c = 4

-------------------------------------------------------------

i = 2

1 is in the set.

So 2 is not a sequence start.

Skip it.

-------------------------------------------------------------

i = 3

2 is in the set.

Skip.

-------------------------------------------------------------

i = 4

3 is in the set.

Skip.

-------------------------------------------------------------

i = 100

99 is not present.

Sequence length = 1.

c remains 4.

-------------------------------------------------------------

i = 200

199 is not present.

Sequence length = 1.

c remains 4.

Final answer:

4

=============================================================
Why This Is O(n)

At first glance, there is a while loop inside a for loop,
which may look like O(n²).

However, the while loop only starts when i is the beginning
of a sequence.

For a sequence such as:

1,2,3,4,5

only 1 starts the while loop.

The numbers 2,3,4,5 are skipped because their previous
numbers exist.

Therefore, each number is processed only a constant
number of times.

Overall:

Time = O(n)

Space = O(n)

=============================================================
Algorithm

1. Put all numbers into a Hash Set.
2. Traverse every unique number.
3. If i - 1 does not exist, i is the start of a sequence.
4. Expand the sequence using x + 1.
5. Track the maximum sequence length.
6. Return the maximum length.
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        n = len(nums)

        if not nums:
            return 0

        c = 1

        s = set(nums)

        for i in s:

            if i - 1 not in s:

                curr = 1
                x = i

                while x + 1 in s:
                    curr += 1
                    x += 1

                c = max(c, curr)

        return c