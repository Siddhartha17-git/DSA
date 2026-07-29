"""
LeetCode 78 - Subsets

Difficulty: Medium

Topics:
- Backtracking

Time Complexity: O(n × 2ⁿ)

There are 2ⁿ possible subsets.
Copying each subset takes O(n).

Space Complexity: O(n)

The recursion stack and current subset together
take at most O(n) space.

=============================================================
Explanation
=============================================================

The idea is simple.

For every element, we have only two choices:

1. Include it in the current subset.
2. Exclude it from the current subset.

By recursively making these two choices for every
element, we generate all possible subsets.

-------------------------------------------------------------

ans = []

Stores all generated subsets.

-------------------------------------------------------------

subset = []

Stores the current subset being built.

As recursion progresses,

elements are added and removed from this list.

-------------------------------------------------------------

backtrack(i, subset)

i represents the current index being processed.

subset represents the current subset.

-------------------------------------------------------------

if i == len(nums)

When all elements have been processed,

store a copy of the current subset.

Example

subset = [1,3]

Store

[1,3]

Return to explore another possibility.

-------------------------------------------------------------

subset.append(nums[i])

Choose to include the current element.

Example

nums = [1,2,3]

Current subset

[1]

Include 2

Subset becomes

[1,2]

-------------------------------------------------------------

backtrack(i + 1, subset)

Continue recursively with the next element.

-------------------------------------------------------------

subset.pop()

Backtracking step.

Remove the recently added element so we can
explore the second choice.

Example

Current subset

[1,2]

After pop()

[1]

-------------------------------------------------------------

backtrack(i + 1, subset)

Now choose NOT to include the current element.

Continue with the next index.

=============================================================
Dry Run

Example

nums = [1,2]

Start

subset = []

-----------------------------

Include 1

subset = [1]

Include 2

subset = [1,2]

Reached end

Store

[1,2]

-----------------------------

Backtrack

subset = [1]

Exclude 2

Store

[1]

-----------------------------

Backtrack

subset = []

Exclude 1

Include 2

Store

[2]

-----------------------------

Backtrack

subset = []

Exclude 2

Store

[]

Final Answer

[
    [1,2],
    [1],
    [2],
    []
]

(The order may vary.)

=============================================================
Recursion Tree

                    []
                  /     \
               +1         -1
             [1]          []
            /   \        /   \
         +2     -2    +2     -2
      [1,2]    [1]   [2]     []

=============================================================
Algorithm

1. Start from index 0 with an empty subset.
2. Include the current element.
3. Recursively process the next index.
4. Backtrack by removing the element.
5. Exclude the current element.
6. Recursively process the next index.
7. When all elements are processed, store the subset.
8. Return all generated subsets.
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []

        def backtrack(i, subset):

            if i == len(nums):
                ans.append(subset[:])
                return

            subset.append(nums[i])

            backtrack(i + 1, subset)

            subset.pop()

            backtrack(i + 1, subset)

        backtrack(0, subset)

        return ans