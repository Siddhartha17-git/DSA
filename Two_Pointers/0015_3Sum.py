"""
LeetCode 15 - 3Sum

Difficulty: Medium

Topics:
- Two Pointers
- Sorting

Time Complexity: O(n²)

Sorting takes O(n log n).

The two-pointer search runs O(n²).

Space Complexity: O(1)

(Excluding the output list.)

=============================================================
Explanation
=============================================================

The idea is to first sort the array.

After sorting, we fix one element and use two pointers
to find the remaining two numbers whose sum is zero.

Sorting also helps us avoid duplicate triplets.

-------------------------------------------------------------

nums.sort()

Sorting arranges the numbers in ascending order.

Example

[-1,0,1,2,-1,-4]

becomes

[-4,-1,-1,0,1,2]

-------------------------------------------------------------

for i in range(n)

Choose nums[i] as the first element of the triplet.

For every first element, search for the remaining
two numbers.

-------------------------------------------------------------

if i > 0 and nums[i] == nums[i-1]:
    continue

If the current element is the same as the previous one,
skip it.

Otherwise, the same triplets would be generated again.

Example

[-1,-1,0,1]

The second -1 is skipped.

-------------------------------------------------------------

j = i + 1

k = n - 1

Initialize two pointers.

j starts immediately after i.

k starts from the end of the array.

-------------------------------------------------------------

while j < k

Continue searching until the pointers meet.

-------------------------------------------------------------

total = nums[i] + nums[j] + nums[k]

Three cases are possible.

-------------------------------------------------------------

If total < 0

The sum is too small.

Move j forward to increase the sum.

j += 1

-------------------------------------------------------------

If total > 0

The sum is too large.

Move k backward to decrease the sum.

k -= 1

-------------------------------------------------------------

Otherwise

A valid triplet is found.

Store it in the answer.

-------------------------------------------------------------

ans.append([nums[i], nums[j], nums[k]])

Save the current triplet.

-------------------------------------------------------------

j += 1

k -= 1

Move both pointers to search for another solution.

-------------------------------------------------------------

while j < k and nums[j] == nums[j-1]:

Skip duplicate values on the left.

Example

...,0,0,0,1,...

Only the first 0 is considered.

-------------------------------------------------------------

while j < k and nums[k] == nums[k+1]:

Skip duplicate values on the right.

This ensures every triplet appears only once.

=============================================================
Dry Run

Example

nums = [-1,0,1,2,-1,-4]

After sorting

[-4,-1,-1,0,1,2]

-------------------------------------------------------------

i = -4

No valid triplet.

-------------------------------------------------------------

i = -1

j = -1

k = 2

Sum = 0

Triplet

[-1,-1,2]

-------------------------------------------------------------

Move pointers

j = 0

k = 1

Sum = 0

Triplet

[-1,0,1]

-------------------------------------------------------------

Duplicate -1 is skipped.

Final Answer

[[-1,-1,2],[-1,0,1]]

=============================================================
Algorithm

1. Sort the array.
2. Fix one element at a time.
3. Use two pointers to find the remaining two numbers.
4. Move pointers based on the current sum.
5. Skip duplicate values.
6. Store every valid triplet.
7. Return the answer.
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        n = len(nums)
        ans = []

        for i in range(n):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1

            while j < k:

                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1

                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1

                else:
                    ans.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return ans