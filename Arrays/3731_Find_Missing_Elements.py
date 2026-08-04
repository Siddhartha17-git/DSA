"""
LeetCode 3731 - Find Missing Elements

Difficulty: Easy

Topics:
- Array
- Hash Set

Time Complexity: O(n + (max - min))

O(n)      -> Build the set and find minimum/maximum.
O(max-min)-> Check every number in the range.

Space Complexity: O(n)

The hash set stores all elements of the array.

=============================================================
Explanation
=============================================================

The array originally contained every integer in a
continuous range.

Some numbers are now missing.

Our task is to find all missing numbers between the
smallest and largest elements.

-------------------------------------------------------------

output = []

Stores all missing numbers.

-------------------------------------------------------------

s = set(nums)

Convert the array into a Hash Set.

This allows checking whether a number exists in O(1)
average time.

Example

nums = [1,4,2,5]

Set

{1,2,4,5}

-------------------------------------------------------------

mini = float("inf")

maxi = float("-inf")

Store the minimum and maximum values.

-------------------------------------------------------------

for i in nums

Traverse the array once.

Update

mini

and

maxi

Example

nums = [5,1,8,3]

After traversal

mini = 1

maxi = 8

-------------------------------------------------------------

for i in range(mini, maxi + 1)

Check every integer in the original range.

-------------------------------------------------------------

if i not in s

The number is missing.

Append it to the answer.

=============================================================
Dry Run

Example

nums = [1,4,2,5]

Set

{1,2,4,5}

Minimum = 1

Maximum = 5

Range

1 2 3 4 5

------------------------

1

Present

------------------------

2

Present

------------------------

3

Missing

Answer = [3]

------------------------

4

Present

------------------------

5

Present

Final Answer

[3]

=============================================================
Algorithm

1. Convert the array into a Hash Set.
2. Find the minimum and maximum elements.
3. Traverse every number between them.
4. If a number is not present in the set, add it to the answer.
5. Return the list of missing numbers.
"""

from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        output = []

        s = set(nums)

        mini = float("inf")
        maxi = float("-inf")

        for i in nums:
            if i < mini:
                mini = i

            if i > maxi:
                maxi = i

        for i in range(mini, maxi + 1):
            if i not in s:
                output.append(i)

        return output