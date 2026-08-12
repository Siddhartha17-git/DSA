"""
LeetCode 347 - Top K Frequent Elements

Difficulty: Medium

Topics:
- Hash Map
- Sorting

Time Complexity: O(n + m log m)

n = number of elements in nums
m = number of unique elements

Building the frequency dictionary takes O(n).

Sorting the unique elements by frequency takes O(m log m).

Space Complexity: O(m)

The dictionary stores every unique element and its frequency.

=============================================================
Explanation
=============================================================

The problem asks us to find the k elements that appear
most frequently in the array.

The solution has two main steps:

1. Count the frequency of every element.
2. Sort the elements based on their frequencies and
   take the first k elements.

-------------------------------------------------------------
Step 1: Count Frequencies
-------------------------------------------------------------

dic = defaultdict(int)

The dictionary stores:

element -> frequency

Example:

nums = [1,1,1,2,2,3]

After traversal:

1 -> 3
2 -> 2
3 -> 1

-------------------------------------------------------------

for i in nums:

    dic[i] += 1

Every time an element appears, increase its frequency.

-------------------------------------------------------------
Step 2: Sort by Frequency
-------------------------------------------------------------

arr = sorted(
    dic.items(),
    key=lambda x: x[1],
    reverse=True
)

dic.items() gives pairs:

(element, frequency)

Example:

[(1,3), (2,2), (3,1)]

The key:

lambda x: x[1]

tells sorted() to use the frequency when sorting.

reverse=True

sorts from highest frequency to lowest frequency.

So:

[(1,3), (2,2), (3,1)]

is already ordered correctly.

-------------------------------------------------------------
Step 3: Take the First k Elements
-------------------------------------------------------------

for i in range(k):

    output.append(arr[i][0])

arr[i][0] is the actual element.

arr[i][1] is its frequency.

We only need the first k elements.

=============================================================
Dry Run

Example:

nums = [1,1,1,2,2,3]

k = 2

-------------------------------------------------------------

Frequency dictionary:

1 -> 3
2 -> 2
3 -> 1

-------------------------------------------------------------

After sorting:

[(1,3), (2,2), (3,1)]

-------------------------------------------------------------

k = 2

Take:

arr[0][0] = 1

arr[1][0] = 2

Answer:

[1,2]

=============================================================
Important Sorting Part

The expression:

sorted(dic.items(), key=lambda x: x[1], reverse=True)

works as follows:

dic.items():

(1,3)
(2,2)
(3,1)

For each pair:

x[0] -> element
x[1] -> frequency

Therefore:

key=lambda x: x[1]

means:

"Sort using the frequency."

reverse=True means:

"Highest frequency first."

=============================================================
Algorithm

1. Create a frequency dictionary.
2. Traverse nums and count every element.
3. Convert the dictionary into a list of
   (element, frequency) pairs.
4. Sort the pairs by frequency in descending order.
5. Take the first k elements.
6. Return the result.
"""

from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dic = defaultdict(int)
        output = []

        for i in nums:
            dic[i] += 1

        arr = sorted(
            dic.items(),
            key=lambda x: x[1],
            reverse=True
        )

        for i in range(k):
            output.append(arr[i][0])

        return output