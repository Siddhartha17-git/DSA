"""
LeetCode 1291 - Sequential Digits

Difficulty: Medium

Topics:
- String

Time Complexity: O(1)

At most 36 sequential numbers are generated
(8 + 7 + 6 + ... + 1 = 36).

Space Complexity: O(1)

=============================================================
Explanation
=============================================================

Instead of checking every number between low and high,
we generate only the possible sequential numbers.

We use the string

"123456789"

because every sequential digit number is simply a
substring of this string.

-------------------------------------------------------------

mi = len(str(low))
ma = len(str(high))

Find the minimum and maximum number of digits that
need to be checked.

Example

low = 100

high = 13000

mi = 3
ma = 5

So we only generate sequential numbers having
3, 4 and 5 digits.

-------------------------------------------------------------

st = "123456789"

This string contains every possible increasing digit.

Examples

Length 2

12
23
34
45
56
67
78
89

Length 3

123
234
345
456
567
678
789

Length 4

1234
2345
3456
4567
5678
6789

-------------------------------------------------------------

for i in range(mi, ma + 1):

Generate sequential numbers having i digits.

-------------------------------------------------------------

for j in range(10 - i):

Slide a window of length i across

"123456789"

Example

i = 4

Windows are

1234
2345
3456
4567
5678
6789

-------------------------------------------------------------

st[j : j + i]

Extract one sequential number as a substring.

Convert it into an integer.

-------------------------------------------------------------

if low <= number <= high

Only keep numbers that lie inside the required range.

-------------------------------------------------------------

output.append(number)

Store the valid sequential number.

Since we generate numbers from left to right and
smaller lengths to larger lengths, the output is
already sorted.

=============================================================
Dry Run

Example

low = 100

high = 300

mi = 3
ma = 3

Generate

123 ✔

234 ✔

345 ✘

456 ✘

...

Output

[123, 234]

=============================================================
Algorithm

1. Find the number of digits in low and high.
2. Use the string "123456789".
3. Generate every substring of valid length.
4. Convert the substring into an integer.
5. If it lies within the range, add it to the answer.
6. Return the result.
"""

from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        mi = len(str(low))
        ma = len(str(high))

        st = "123456789"
        output = []

        for i in range(mi, ma + 1):
            for j in range(10 - i):
                if int(st[j:j + i]) >= low and int(st[j:j + i]) <= high:
                    output.append(int(st[j:j + i]))

        return output