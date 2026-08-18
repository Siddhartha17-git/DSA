"""
LeetCode 904 - Fruit Into Baskets

Difficulty: Medium

Topics:
- Sliding Window
- Hash Map
- Array

Time Complexity: O(n)

Each fruit is added to the window once and removed
from the window at most once.

Space Complexity: O(1)

The dictionary contains at most 3 fruit types temporarily,
and the valid window contains at most 2 types.

=============================================================
Explanation
=============================================================

We need to find the longest contiguous subarray containing
at most TWO different fruit types.

This is a classic Sliding Window problem.

The window is:

    fruits[i ... j]

where:

i = left boundary
j = right boundary

The dictionary stores the frequency of every fruit type
inside the current window.

-------------------------------------------------------------
Initialization
-------------------------------------------------------------

answer = 0

Stores the maximum number of fruits collected.

-------------------------------------------------------------

maxi = 0

This variable is not actually used in the solution.

It can be removed without changing the algorithm.

-------------------------------------------------------------

dic = defaultdict(int)

Stores:

fruit type -> frequency inside current window

-------------------------------------------------------------

i = 0

Left pointer of the sliding window.

=============================================================
Expanding the Window
=============================================================

for j in range(len(fruits)):

Move the right pointer through the array.

-------------------------------------------------------------

dic[fruits[j]] += 1

Add the current fruit to the window.

Example:

fruits = [1,2,1]

After processing:

1

dic = {1:1}

Then 2:

dic = {1:1, 2:1}

Then another 1:

dic = {1:2, 2:1}

The window still contains only two fruit types.

=============================================================
When the Window Becomes Invalid
=============================================================

while len(dic) > 2:

We have more than two different fruit types.

Therefore, the current window cannot be used.

We must shrink it from the left.

-------------------------------------------------------------

dic[fruits[i]] -= 1

Remove one occurrence of the fruit at the left.

-------------------------------------------------------------

if dic[fruits[i]] == 0:

If there are no more occurrences of that fruit
inside the window, remove its entry from the dictionary.

-------------------------------------------------------------

del dic[fruits[i]]

This is important because len(dic) represents the
number of different fruit types currently inside
the window.

-------------------------------------------------------------

i += 1

Move the left pointer forward.

Continue shrinking until only two fruit types remain.

=============================================================
Updating the Answer
=============================================================

answer = max(answer, j - i + 1)

Once the window contains at most two fruit types,
it is valid.

Its length is:

    j - i + 1

Keep the largest valid window.

=============================================================
Dry Run

fruits = [1,2,3,2,2]

-------------------------------------------------------------

j = 0

Window:

[1]

dic = {1:1}

answer = 1

-------------------------------------------------------------

j = 1

Window:

[1,2]

dic = {1:1, 2:1}

answer = 2

-------------------------------------------------------------

j = 2

Add 3:

dic = {1:1, 2:1, 3:1}

There are 3 fruit types.

Invalid.

Shrink from the left.

Remove 1:

dic = {2:1, 3:1}

i = 1

Window:

[2,3]

length = 2

-------------------------------------------------------------

j = 3

Add another 2:

dic = {2:2, 3:1}

Window:

[2,3,2]

length = 3

answer = 3

-------------------------------------------------------------

j = 4

Add another 2:

dic = {2:3, 3:1}

Window:

[2,3,2,2]

length = 4

answer = 4

Final answer:

4

=============================================================
Why Sliding Window Works

The condition is:

    At most 2 different fruit types.

If the window has 2 or fewer types,
we can safely expand it.

If it has more than 2 types,
we shrink it from the left until it becomes valid again.

This allows us to find the longest valid subarray
without checking every possible subarray.

=============================================================
Algorithm

1. Create a frequency dictionary.
2. Set the left pointer i = 0.
3. Move the right pointer j through the array.
4. Add fruits[j] to the dictionary.
5. If there are more than 2 fruit types:
   - Remove fruits[i].
   - Delete its dictionary entry if its count becomes 0.
   - Move i forward.
6. Calculate the current window length.
7. Keep the maximum length.
8. Return the answer.
"""

from collections import defaultdict
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        answer = 0
        maxi = 0

        dic = defaultdict(int)

        i = 0

        for j in range(len(fruits)):

            dic[fruits[j]] += 1

            while len(dic) > 2:

                dic[fruits[i]] -= 1

                if dic[fruits[i]] == 0:
                    del dic[fruits[i]]

                i += 1

            answer = max(answer, j - i + 1)

        return answer