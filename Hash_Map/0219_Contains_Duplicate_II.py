"""
LeetCode 219 - Contains Duplicate II

Difficulty: Easy

Topics:
- Hash Map
- Array

Time Complexity: O(n)

The array is traversed only once.

Space Complexity: O(n)

The Hash Map can store up to n elements.

=============================================================
Explanation
=============================================================

We need to find whether the same number occurs twice
within a distance of k indices.

Instead of storing every occurrence of a number,
we store only its MOST RECENT index.

Why?

If the current occurrence is not within distance k
from the previous occurrence, then an older occurrence
will be even farther away and cannot be useful.

Therefore, we can safely replace the stored index
with the current index.

-------------------------------------------------------------

s = {}

The dictionary stores:

number -> most recent index

Example:

nums = [1,2,3,1]

After processing the first 1:

s = {1: 0}

-------------------------------------------------------------

for i in range(len(nums))

Traverse the array from left to right.

-------------------------------------------------------------

if nums[i] not in s:

This is the first time we have seen this number.

Store its index.

s[nums[i]] = i

-------------------------------------------------------------

else:

The number has appeared before.

The stored index is the most recent previous
occurrence.

-------------------------------------------------------------

abs(i - s[nums[i]]) <= k

Check whether the distance between the current
index and the previous occurrence is at most k.

If yes, we found a valid pair.

Return True.

-------------------------------------------------------------

else:

The previous occurrence is too far away.

Since the current index is more recent, replace
the stored index.

s[nums[i]] = i

This is important because a future occurrence should
be compared with the closest previous occurrence.

=============================================================
Dry Run

Example:

nums = [1,2,3,1]

k = 3

-------------------------------------------------------------

i = 0

nums[0] = 1

1 is not in dictionary.

s = {1: 0}

-------------------------------------------------------------

i = 1

nums[1] = 2

s = {1: 0, 2: 1}

-------------------------------------------------------------

i = 2

nums[2] = 3

s = {1: 0, 2: 1, 3: 2}

-------------------------------------------------------------

i = 3

nums[3] = 1

1 already exists.

Previous index = 0

Distance:

|3 - 0| = 3

k = 3

3 <= 3

Therefore return True.

=============================================================
Why We Update the Index

Example:

nums = [1,2,3,1,1]

k = 1

When we reach index 3:

Previous 1 is at index 0.

Distance = 3

Too far.

So we update:

s[1] = 3

At index 4:

Distance = |4 - 3|

= 1

Now the condition is satisfied.

Therefore return True.

=============================================================
Algorithm

1. Create a dictionary to store the latest index
   of every number.
2. Traverse the array.
3. If the number has not appeared before, store
   its current index.
4. If it has appeared, calculate the index distance.
5. If the distance is <= k, return True.
6. Otherwise update its stored index.
7. If no valid pair is found, return False.
"""

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = {}

        for i in range(len(nums)):

            if nums[i] not in s:
                s[nums[i]] = i

            else:
                if abs(i - s[nums[i]]) <= k:
                    return True

                else:
                    s[nums[i]] = i

        return False