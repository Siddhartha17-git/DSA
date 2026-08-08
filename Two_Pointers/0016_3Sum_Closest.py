"""
LeetCode 16 - 3Sum Closest

Difficulty: Medium

Topics:
- Two Pointers
- Sorting

Time Complexity: O(n²)

Sorting takes O(n log n), and the nested two-pointer
search takes O(n²).

Space Complexity: O(1)

Ignoring the space used by sorting and the answer.

=============================================================
Explanation
=============================================================

The idea is to sort the array and then use two pointers
to find a three-element sum closest to the target.

We fix one element using i and use two pointers,
j and k, to search for the other two elements.

-------------------------------------------------------------

nums.sort()

Sort the array in ascending order.

Sorting allows us to decide how to move the two pointers
based on whether the current sum is smaller or larger
than the target.

Example:

[-1, 2, 1, -4]

becomes

[-4, -1, 1, 2]

-------------------------------------------------------------

ans = 0

Stores the sum that is currently closest to the target.

-------------------------------------------------------------

x = float("inf")

Stores the smallest difference found so far.

Initially, we haven't found any sum, so the difference
is set to infinity.

-------------------------------------------------------------

for i in range(len(nums))

Fix nums[i] as the first number.

The remaining two numbers must come from the part
after i.

-------------------------------------------------------------

j = i + 1
k = n - 1

j starts immediately after i.

k starts at the last element.

These two pointers search for the best pair.

-------------------------------------------------------------

summ = nums[i] + nums[j] + nums[k]

Calculate the current three-number sum.

-------------------------------------------------------------

diff = abs(target - summ)

Find how far the current sum is from the target.

Example:

target = 1

summ = 2

diff = |1 - 2|

= 1

-------------------------------------------------------------

if diff < x:

If this sum is closer to the target than the previous
best sum, update both x and ans.

x = diff

ans = summ

-------------------------------------------------------------

if summ < target:

The current sum is smaller than the target.

Because the array is sorted, increasing j will increase
the sum.

Therefore:

j += 1

-------------------------------------------------------------

else:

The current sum is greater than or equal to the target.

Move k backward to decrease the sum.

k -= 1

=============================================================
Dry Run

nums = [-1,2,1,-4]

target = 1

After sorting:

[-4,-1,1,2]

-------------------------------------------------------------

i = 0

nums[i] = -4

j = 1

k = 3

Sum:

-4 + (-1) + 2 = -3

Difference:

|1 - (-3)| = 4

ans = -3

Since sum < target,

j += 1

-------------------------------------------------------------

Next:

-4 + 1 + 2 = -1

Difference = 2

ans = -1

-------------------------------------------------------------

Next i

nums[i] = -1

j = 2

k = 3

Sum:

-1 + 1 + 2 = 2

Difference:

|1 - 2| = 1

ans = 2

Since 2 > 1,

k -= 1

Pointers meet.

Final answer:

2

=============================================================
Why Two Pointers Work

After sorting:

If

summ < target

we need a larger sum.

Moving j forward gives us a larger value.

If

summ > target

we need a smaller sum.

Moving k backward gives us a smaller value.

Therefore, every pointer movement is directed toward
the target instead of checking every possible triplet.

=============================================================
Algorithm

1. Sort the array.
2. Fix nums[i] as the first element.
3. Set j = i + 1 and k = n - 1.
4. Calculate the current three-number sum.
5. Update the closest answer if necessary.
6. If the sum is smaller than target, move j forward.
7. Otherwise, move k backward.
8. Continue until j and k meet.
9. Return the closest sum.
"""

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        n = len(nums)

        ans = 0
        x = float("inf")

        for i in range(len(nums)):
            j = i + 1
            k = n - 1

            while j < k:

                summ = nums[i] + nums[j] + nums[k]

                diff = abs(target - summ)

                if diff < x:
                    x = diff
                    ans = summ

                if summ < target:
                    j += 1
                else:
                    k -= 1

        return ans