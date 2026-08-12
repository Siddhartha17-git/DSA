"""
LeetCode 2958 - Length of Longest Subarray With at Most K Frequency

Difficulty: Medium

Topics:
- Sliding Window
- Hash Map
- Array

Time Complexity: O(n)

Each element is added to the window once and removed
from the window at most once.

Space Complexity: O(n)

The dictionary can contain up to n different elements.

=============================================================
Explanation
=============================================================

We need to find the longest contiguous subarray where
every element appears at most k times.

We use a Sliding Window.

The window is represented by:

    [i ... j]

where:

i = left boundary
j = right boundary

The dictionary stores the frequency of each element
inside the current window.

-------------------------------------------------------------
Initialization
-------------------------------------------------------------

i = 0
j = 0

The left pointer starts at the beginning.

-------------------------------------------------------------

maxilen = 0

Stores the maximum valid window length found so far.

-------------------------------------------------------------

dic = defaultdict(int)

Stores:

element -> frequency inside current window

=============================================================
Expanding the Window
=============================================================

for a in nums:

Each new element is added to the current window.

-------------------------------------------------------------

dic[a] += 1

Increase the frequency of the current element.

-------------------------------------------------------------

Example:

nums = [1,2,1,2,1]

k = 2

When processing the third 1:

dic = {
    1: 2,
    2: 1
}

The window is still valid.

When processing another 1:

dic[1] = 3

Now the window is invalid because frequency > k.

=============================================================
Shrinking the Window
=============================================================

while dic[a] > k:

The current element has appeared too many times.

Therefore, we move the left pointer forward.

-------------------------------------------------------------

dic[nums[i]] -= 1

Remove nums[i] from the current window.

-------------------------------------------------------------

i += 1

Move the left boundary forward.

Continue until the frequency of the newly added element
becomes <= k.

At that point, the window is valid again.

=============================================================
Updating the Answer
=============================================================

j += 1

Move the right side of the window forward.

-------------------------------------------------------------

maxilen = max(maxilen, j - i)

The current window length is:

    j - i

because j represents the number of elements processed
so far.

Keep the largest valid window.

=============================================================
Dry Run

nums = [1,2,1,2,1,2]

k = 2

-------------------------------------------------------------

Add 1

Window:

[1]

frequency:

1 -> 1

length = 1

max = 1

-------------------------------------------------------------

Add 2

Window:

[1,2]

frequency:

1 -> 1
2 -> 1

length = 2

max = 2

-------------------------------------------------------------

Add 1

Window:

[1,2,1]

frequency:

1 -> 2
2 -> 1

length = 3

max = 3

-------------------------------------------------------------

Add 2

Window:

[1,2,1,2]

frequency:

1 -> 2
2 -> 2

length = 4

max = 4

-------------------------------------------------------------

Add 1

frequency:

1 -> 3

This violates k = 2.

Shrink from the left:

Remove first 1.

frequency:

1 -> 2

Now valid.

Window:

[2,1,2,1]

length = 4

max = 4

-------------------------------------------------------------

Add 2

frequency:

2 -> 3

Again invalid.

Remove the leftmost element:

Remove 2.

frequency:

2 -> 2

Window becomes:

[1,2,1,2]

length = 4

Final answer:

4

=============================================================
Why Sliding Window Works

The important property is:

If a window contains an element more than k times,
we cannot keep that entire window.

So we shrink the window from the left until it becomes
valid again.

Once the window is valid, we try to expand it again.

We never move the left pointer backwards.

Therefore, both pointers together move at most n times.

This gives O(n) time.

=============================================================
Algorithm

1. Create a frequency dictionary.
2. Start the left pointer at 0.
3. Add each new element to the window.
4. If its frequency becomes greater than k,
   move the left pointer forward.
5. Decrease frequencies while shrinking.
6. Calculate the current window length.
7. Keep the maximum length.
8. Return the maximum length.
"""

from collections import defaultdict
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        i, j = 0, 0

        maxilen = 0

        dic = defaultdict(int)

        for a in nums:

            dic[a] += 1

            while dic[a] > k:
                dic[nums[i]] -= 1
                i += 1

            j += 1

            maxilen = max(maxilen, j - i)

        return maxilen