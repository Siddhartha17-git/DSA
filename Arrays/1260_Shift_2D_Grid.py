"""
LeetCode 1260 - Shift 2D Grid

Difficulty: Easy

Topics:
- Array
- Matrix

Time Complexity: O(m × n)

Every element is visited exactly once.

Space Complexity: O(m × n)

A new grid is created to store the shifted values.

=============================================================
Explanation
=============================================================

Rather than shifting the grid incrementally by one step at a time,
we compute the exact location of each element following k shifts.

We accomplish this by mapping the 2D position to a 1D index, shifting it,
and then remapping it back to the 2D coordinate space.

------------------------------------------------------------------------------

m, n = len(grid), len(grid[0])

m  Number of rows

n  Number of columns

grida = [[0] * n for _ in range(m)]

Construct a grid of the same dimensions where we'll
store our shifted values.


for i in range(m):
    for j in range(n):

Iterate through each element in the grid.

idx = i * n + j

Map the 2D position to a 1D index.

Example

Grid

Indices
shift_idx = (idx + k) % (m * n)

Shift the index and wrap it around using the
modulo operator.

Example

Total number of elements = 9

Current index = 8

k = 1

New index

(8 + 1) % 9 = 0

Therefore, the last element moves to the beginning.


idx_i = shift_idx // n

Calculate the new row.


idx_j = shift_idx % n

Calculate the new column.

grida[idx_i][idx_j] = grid[i][j]

Insert the element at the computed index.
=============================================================
Dry Run

Example

grid =

1 2 3
4 5 6
7 8 9

k = 1

Element 1

Index = 0

New Index = 1

Placed at

(0,1)

-------------------------------------------------------------

Element 9

Index = 8

New Index = 0

Placed at

(0,0)

Final Grid

9 1 2
3 4 5
6 7 8

=============================================================
Algorithm

1. Find the dimensions of the grid.
2. Create an empty grid of the same size.
3. Convert every element's position into a 1D index.
4. Shift the index by k positions.
5. Convert the shifted index back to 2D coordinates.
6. Place the element in its new position.
7. Return the shifted grid.
"""

from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        grida = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):

                idx = i * n + j

                shift_idx = (idx + k) % (m * n)

                idx_i = shift_idx // n
                idx_j = shift_idx % n

                grida[idx_i][idx_j] = grid[i][j]

        return grida