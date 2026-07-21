"""
LeetCode 3499 - Maximize Active Section with Trade I

Difficulty: Medium

Topics:
- Array
- String

Time Complexity: O(n)

The string is traversed twice.

Space Complexity: O(n)

The zero block lengths are stored in an array.

=============================================================
Explanation
=============================================================

The idea is to first count how many active ('1')
sections already exist.

Then, instead of simulating every possible trade,
we observe that making one trade can merge two
adjacent zero blocks into one larger active block.

So we only need the lengths of every consecutive
block of zeros.

-------------------------------------------------------------

ones = 0

Counts the total number of active sections already
present in the string.

Example

s = "1000100"

ones = 2

-------------------------------------------------------------

zero_blocks = []

Stores the length of every consecutive block of zeros.

Example

s = "1000100"

Zero blocks

"000" → length = 3

"00" → length = 2

zero_blocks = [3,2]

-------------------------------------------------------------

while i < n

Traverse the string.

Whenever a zero is found,

find the complete consecutive block.

-------------------------------------------------------------

j = i

while j < n and s[j] == "0":

Move j until the zero block ends.

Length of the block

j - i

Store it inside zero_blocks.

Example

s =

100001100

First block

0000

Length = 4

-------------------------------------------------------------

ans = 0

Stores the maximum number of inactive sections
that can become active after one trade.

-------------------------------------------------------------

for i in range(len(zero_blocks)-1)

A single trade can merge only two neighbouring
zero blocks.

So check every adjacent pair.

-------------------------------------------------------------

ans = max(ans,
          zero_blocks[i] + zero_blocks[i+1])

Example

zero_blocks

[3,2,4]

Possible merged lengths

3+2 = 5

2+4 = 6

Maximum = 6

-------------------------------------------------------------

return ans + ones

The final answer is

Existing active sections

+

Maximum merged zero sections

=============================================================
Dry Run

Example

s = "1000100"

ones = 2

zero_blocks = [3,2]

Maximum merged block

3 + 2 = 5

Answer

2 + 5 = 7

=============================================================
Algorithm

1. Count the total number of '1's.
2. Find the length of every consecutive zero block.
3. Store each block length.
4. Check every pair of adjacent zero blocks.
5. Find the maximum merged length.
6. Add it to the original count of ones.
7. Return the answer.
"""

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)

        ones = 0

        for i in s:
            if i == "1":
                ones += 1

        zero_blocks = []

        i = 0

        while i < n:

            if s[i] == "0":

                j = i

                while j < n and s[j] == "0":
                    j += 1

                zero_blocks.append(j - i)

                i = j

            else:
                i += 1

        ans = 0

        for i in range(len(zero_blocks) - 1):
            ans = max(ans, zero_blocks[i] + zero_blocks[i + 1])

        return ans + ones