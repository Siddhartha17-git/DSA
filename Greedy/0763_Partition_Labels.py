"""
LeetCode 763 - Partition Labels

Difficulty: Medium

Topics:
- Greedy
- Hash Map

Time Complexity: O(n)

The string is traversed twice.

Space Complexity: O(1)

At most 26 lowercase letters are stored.

=============================================================
Explanation
=============================================================

The idea is to partition the string into the maximum
number of parts such that every character appears in
only one partition.

To do this, we first find the last occurrence of every
character.

Then we greedily extend the current partition until all
characters inside it finish.

-------------------------------------------------------------

letter_dict = {}

Stores the last occurrence (last index) of every
character.

Example

s = "abac"

letter_dict

a → 2

b → 1

c → 3

-------------------------------------------------------------

for i in range(len(s))

Traverse the string once.

For every character,

store its latest index.

Since later occurrences overwrite earlier ones,

the dictionary finally stores the last occurrence.

-------------------------------------------------------------

start = 0

Marks the starting index of the current partition.

-------------------------------------------------------------

maxx = -1

Stores the farthest index that the current partition
must reach.

Initially,

no characters have been processed.

-------------------------------------------------------------

for i in range(len(s))

Traverse the string again.

-------------------------------------------------------------

maxx = max(letter_dict[s[i]], maxx)

For the current character,

find its last occurrence.

If it lies beyond the current partition,

extend the partition.

Example

Current partition

ababc

Current character

'a'

Last occurrence

8

Partition must extend until index 8.

-------------------------------------------------------------

if i == maxx

When the current index reaches the farthest required
index,

every character inside this partition has completely
finished appearing.

So we can safely create one partition.

-------------------------------------------------------------

ans.append(i - start + 1)

Store the size of the current partition.

Example

start = 0

i = 8

Partition size

8 - 0 + 1 = 9

-------------------------------------------------------------

start = i + 1

The next partition starts immediately after the
current one.

=============================================================
Dry Run

Example

s = "ababcbacadefegdehijhklij"

Last occurrences

a → 8

b → 5

c → 7

...

-------------------------------------------------------------

Start

start = 0

maxx = 8

Traverse

0 → 8

At index 8

Partition size

9

-------------------------------------------------------------

Next partition

start = 9

maxx = 15

Traverse

9 → 15

Partition size

7

-------------------------------------------------------------

Next partition

start = 16

maxx = 23

Traverse

16 → 23

Partition size

8

Answer

[9,7,8]

=============================================================
Algorithm

1. Store the last occurrence of every character.
2. Traverse the string again.
3. Keep extending the current partition using the
   farthest last occurrence.
4. When the current index reaches that farthest index,
   record the partition size.
5. Start a new partition.
6. Return all partition sizes.
"""

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letter_dict = {}
        ans = []

        start = 0

        for i in range(len(s)):
            letter_dict[s[i]] = i

        maxx = -1

        for i in range(len(s)):
            maxx = max(letter_dict[s[i]], maxx)

            if i == maxx:
                ans.append(i - start + 1)
                start = i + 1

        return ans