"""
LeetCode 3016 - Minimum Number of Pushes to Type Word II

Difficulty: Medium

Topics:
- Greedy
- Hash Map
- Sorting

Time Complexity: O(n + k log k)

n = length of the word
k = number of distinct characters (k ≤ 26)

Counting frequencies takes O(n).
Sorting at most 26 frequencies is O(k log k).

Space Complexity: O(k)

Stores the frequency of each distinct character.

=============================================================
Explanation
=============================================================

Unlike Part I,

letters can repeat.

To minimize the total number of pushes,

the most frequently occurring letters should
require the fewest pushes.

Therefore,

1. Count the frequency of every character.
2. Sort the frequencies in descending order.
3. Assign

   First 8 frequencies  -> 1 push

   Next 8 frequencies   -> 2 pushes

   Next 8 frequencies   -> 3 pushes

   Remaining            -> 4 pushes

-------------------------------------------------------------

d = {}

Stores the frequency of every character.

Example

word = "aabbccc"

Dictionary

a → 2

b → 2

c → 3

-------------------------------------------------------------

for ch in word

Count how many times every character appears.

-------------------------------------------------------------

freq_sorted = sorted(d.values(), reverse=True)

Extract only the frequencies and sort them
from largest to smallest.

Example

Frequencies

[2,5,3,1]

After sorting

[5,3,2,1]

-------------------------------------------------------------

for i, f in enumerate(freq_sorted)

i represents the position assigned to the
character.

The first eight frequencies receive

1 push.

The next eight receive

2 pushes.

-------------------------------------------------------------

(i // 8) + 1

Calculates the number of pushes.

Examples

i = 0

1 push

----------------

i = 7

1 push

----------------

i = 8

2 pushes

----------------

i = 16

3 pushes

-------------------------------------------------------------

count += ((i // 8) + 1) * f

Multiply

(pushes required)

×

(number of occurrences)

and add it to the answer.

=============================================================
Dry Run

Example

word = "aabbccddeeffgghhiiiiii"

Frequency

i → 6

a → 2

b → 2

c → 2

d → 2

e → 2

f → 2

g → 2

h → 2

Sorted Frequencies

[6,2,2,2,2,2,2,2,2]

Assignments

6 × 1

2 × 1

2 × 1

2 × 1

2 × 1

2 × 1

2 × 1

2 × 1

2 × 2

Total

6 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 4

= 24

=============================================================
Algorithm

1. Count the frequency of every character.
2. Sort the frequencies in descending order.
3. Assign the first 8 frequencies to 1 push.
4. Assign the next 8 frequencies to 2 pushes.
5. Continue similarly for the remaining frequencies.
6. Multiply each frequency by its push count.
7. Return the total pushes.
"""

from typing import List


class Solution:
    def minimumPushes(self, word: str) -> int:
        d = {}

        for ch in word:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1

        freq_sorted = sorted(d.values(), reverse=True)

        count = 0

        for i, f in enumerate(freq_sorted):
            count += ((i // 8) + 1) * f

        return count