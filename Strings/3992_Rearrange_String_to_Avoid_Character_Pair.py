"""
LeetCode 3992 - Rearrange String to Avoid Character Pair

Difficulty: Easy

Topics:
- String

Time Complexity: O(n)

Space Complexity: O(n)

=============================================================
Explanation
=============================================================

The goal is to rearrange the string so that every
occurrence of y appears before every occurrence of x.

Instead of sorting the string, we divide the characters
into three groups.

-------------------------------------------------------------

resy = ""

Stores every occurrence of y.

-------------------------------------------------------------

resx = ""

Stores every occurrence of x.

-------------------------------------------------------------

resn = ""

Stores every remaining character.

-------------------------------------------------------------

for i in s

Traverse every character.

-------------------------------------------------------------

if i == y

Store every y first.

-------------------------------------------------------------

elif i == x

Store every x separately.

-------------------------------------------------------------

else

Store every other character in resn.

-------------------------------------------------------------

return resy + resn + resx

Build the final string.

Every y appears first.

Other characters remain in the middle.

Every x appears at the end.

Therefore,

every occurrence of y appears before every occurrence
of x.

=============================================================
Dry Run

Example

s = "aabc"

x = "a"

y = "c"

After traversal

resy = "c"

resn = "b"

resx = "aa"

Result

"cbaa"

=============================================================
Algorithm

1. Create three empty strings.
2. Traverse the input string.
3. Store y characters separately.
4. Store x characters separately.
5. Store remaining characters.
6. Concatenate

resy + resn + resx

and return it.
"""

class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:

        resx = ""
        resy = ""
        resn = ""

        for i in s:

            if i == y:
                resy += i

            elif i == x:
                resx += i

            else:
                resn += i

        return resy + resn + resx