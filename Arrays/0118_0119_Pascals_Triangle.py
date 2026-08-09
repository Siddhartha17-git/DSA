"""
LeetCode 118 + 119 - Pascal's Triangle I & II

Difficulty:
- 118: Easy
- 119: Easy

Topics:
- Array
- Dynamic Programming

=============================================================
LeetCode 118 - Pascal's Triangle
=============================================================

Given numRows, generate the first numRows rows
of Pascal's Triangle.

-------------------------------------------------------------

Idea

Every row starts and ends with 1.

The elements in between are calculated using
the previous row:

row[j] = previous_row[j-1] + previous_row[j]

Example:

        1
       1 1
      1 2 1
     1 3 3 1

For example, to calculate 3:

1 + 2 = 3

-------------------------------------------------------------

row = [1] * (i + 1)

Create a row containing only 1s.

For example, when i = 3:

row = [1,1,1,1]

-------------------------------------------------------------

for j in range(1, i):

Only the middle elements need to be calculated.

The first and last elements remain 1.

-------------------------------------------------------------

row[j] = output[i-1][j-1] + output[i-1][j]

Use the two elements directly above the current
position to calculate the value.

-------------------------------------------------------------

output.append(row)

Store the completed row.

=============================================================
LeetCode 119 - Pascal's Triangle II
=============================================================

Instead of returning the complete triangle,
return only the row at rowIndex.

The implementation uses the same logic as
LeetCode 118.

-------------------------------------------------------------

rows = rowIndex + 1

If rowIndex = 3,

we need to generate 4 rows:

0, 1, 2, 3

-------------------------------------------------------------

Generate every row using the same method as
LeetCode 118.

At the end:

return output[-1]

returns the requested row.

=============================================================
Dry Run

numRows = 5

i = 0

[1]

i = 1

[1,1]

i = 2

[1,2,1]

i = 3

[1,3,3,1]

i = 4

[1,4,6,4,1]

Final output:

[
 [1],
 [1,1],
 [1,2,1],
 [1,3,3,1],
 [1,4,6,4,1]
]

-------------------------------------------------------------

For LeetCode 119:

rowIndex = 3

Generate until row 3.

Return:

[1,3,3,1]

=============================================================
Complexity

LeetCode 118:

Time Complexity: O(numRows²)

Space Complexity: O(numRows²)

because the complete triangle is stored.

-------------------------------------------------------------

LeetCode 119 using this implementation:

Time Complexity: O(rowIndex²)

Space Complexity: O(rowIndex²)

because all rows up to rowIndex are stored.

=============================================================
"""

from typing import List


class Solution:
    # LeetCode 118 - Pascal's Triangle
    def generate(self, numRows: int) -> List[List[int]]:
        output = []

        for i in range(numRows):

            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = output[i - 1][j - 1] + output[i - 1][j]

            output.append(row)

        return output

    # LeetCode 119 - Pascal's Triangle II
    def getRow(self, rowIndex: int) -> List[int]:
        rows = rowIndex + 1

        output = []

        for i in range(rows):

            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = output[i - 1][j - 1] + output[i - 1][j]

            output.append(row)

        return output[-1]