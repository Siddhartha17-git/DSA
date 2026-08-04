"""
LeetCode 36 - Valid Sudoku

Difficulty: Medium

Topics:
- Hash Set
- Array
- Matrix

Time Complexity: O(1)

The board size is fixed (9 × 9).

Rows  : 9 × 9 = 81 checks

Columns : 9 × 9 = 81 checks

Subgrids : 9 × 9 = 81 checks

Total operations are constant.

Space Complexity: O(1)

Each set stores at most 9 digits.

=============================================================
Explanation
=============================================================

A Sudoku board is valid if

1. Every row contains unique digits.
2. Every column contains unique digits.
3. Every 3×3 subgrid contains unique digits.

Since the board size is fixed,

we simply check these three conditions separately.

=============================================================
Checking Rows

-------------------------------------------------------------

for i in range(9):

Process one row at a time.

-------------------------------------------------------------

srow = set()

Stores all digits already seen in the current row.

-------------------------------------------------------------

for j in range(9)

Traverse every column of the current row.

-------------------------------------------------------------

if board[i][j] == "."

Empty cells are ignored.

-------------------------------------------------------------

elif board[i][j] in srow

The digit already exists in the row.

Duplicate found.

Return False.

-------------------------------------------------------------

else

Add the digit to the set.

=============================================================
Checking Columns

-------------------------------------------------------------

for i in range(9)

Process one column.

-------------------------------------------------------------

scol = set()

Stores digits already seen in this column.

-------------------------------------------------------------

board[j][i]

Notice the indices are reversed.

j changes the row.

i remains the fixed column.

-------------------------------------------------------------

Duplicate found?

Return False.

Otherwise

Insert into the set.

=============================================================
Checking 3 × 3 Subgrids

There are exactly

9 subgrids.

We number them

0 1 2

3 4 5

6 7 8

-------------------------------------------------------------

for grid in range(9)

Process one subgrid.

-------------------------------------------------------------

row = (grid // 3) * 3

Find the starting row.

grid = 0

0 // 3 = 0

row = 0

------------------------

grid = 4

4 // 3 = 1

row = 3

------------------------

grid = 8

8 // 3 = 2

row = 6

-------------------------------------------------------------

col = (grid % 3) * 3

Find the starting column.

grid = 0

0 % 3 = 0

col = 0

------------------------

grid = 1

1 % 3 = 1

col = 3

------------------------

grid = 2

2 % 3 = 2

col = 6

-------------------------------------------------------------

Example

grid = 5

row = (5 // 3) * 3

= 1 × 3

= 3

col = (5 % 3) * 3

= 2 × 3

= 6

So we start checking

Rows

3,4,5

Columns

6,7,8

-------------------------------------------------------------

sgrid = set()

Stores digits already seen inside this 3×3 box.

-------------------------------------------------------------

for i in range(row, row + 3)

for j in range(col, col + 3)

Visit every cell of the subgrid.

-------------------------------------------------------------

If the digit already exists,

return False.

Otherwise,

insert it into the set.

=============================================================
Dry Run

Example

Top-left subgrid

5 3 .

6 . .

. 9 8

Set progression

{}

↓

{5}

↓

{5,3}

↓

{5,3,6}

↓

{5,3,6,9}

↓

{5,3,6,9,8}

No duplicates.

Move to the next subgrid.

=============================================================
Algorithm

1. Check every row using a Hash Set.
2. Check every column using a Hash Set.
3. Compute the starting position of each 3×3 subgrid.
4. Check every subgrid using another Hash Set.
5. If any duplicate is found, return False.
6. Otherwise return True.
"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows
        for i in range(9):
            srow = set()

            for j in range(9):

                if board[i][j] == ".":
                    continue

                elif board[i][j] in srow:
                    return False

                else:
                    srow.add(board[i][j])

        # Check columns
        for i in range(9):
            scol = set()

            for j in range(9):

                if board[j][i] == ".":
                    continue

                elif board[j][i] in scol:
                    return False

                else:
                    scol.add(board[j][i])

        # Check 3×3 subgrids
        for grid in range(9):

            row = (grid // 3) * 3
            col = (grid % 3) * 3

            sgrid = set()

            for i in range(row, row + 3):
                for j in range(col, col + 3):

                    if board[i][j] == ".":
                        continue

                    elif board[i][j] in sgrid:
                        return False

                    else:
                        sgrid.add(board[i][j])

        return True