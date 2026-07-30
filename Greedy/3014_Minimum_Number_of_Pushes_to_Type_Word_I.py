"""
LeetCode 3014 - Minimum Number of Pushes to Type Word I

Difficulty: Easy

Topics:
- Greedy
- Math

Time Complexity: O(n)

The word is traversed only once.

Space Complexity: O(1)

=============================================================
Explanation
=============================================================

There are 8 keys available
(keys 2 to 9).

To minimize the total number of pushes,

we assign

• First 8 letters  -> 1 push
• Next 8 letters   -> 2 pushes
• Next 8 letters   -> 3 pushes
• Remaining letters -> 4 pushes

Since every letter in the word is distinct,

only the length of the word matters.

-------------------------------------------------------------

count = 0

Stores the total number of pushes.

-------------------------------------------------------------

n = len(word)

Number of distinct letters.

-------------------------------------------------------------

for i in range(n)

Process each letter.

The index determines how many pushes are needed.

-------------------------------------------------------------

(i // 8) + 1

Every group of 8 letters requires one additional push.

Examples

i = 0

0 // 8 + 1 = 1 push

----------------------

i = 7

7 // 8 + 1 = 1 push

----------------------

i = 8

8 // 8 + 1 = 2 pushes

----------------------

i = 15

15 // 8 + 1 = 2 pushes

----------------------

i = 16

16 // 8 + 1 = 3 pushes

-------------------------------------------------------------

count += (i // 8) + 1

Add the required pushes for the current letter.

=============================================================
Dry Run

Example

word = "xycdefghij"

Length = 10

Indices

0 1 2 3 4 5 6 7 8 9

Pushes

1 1 1 1 1 1 1 1 2 2

Total

8 + 4

= 12

=============================================================
Algorithm

1. Find the length of the word.
2. Process each character position.
3. Every block of 8 letters requires one extra push.
4. Add the push count for every position.
5. Return the total number of pushes.
"""

class Solution:
    def minimumPushes(self, word: str) -> int:
        count = 0
        n = len(word)

        for i in range(n):
            count += (i // 8) + 1

        return count