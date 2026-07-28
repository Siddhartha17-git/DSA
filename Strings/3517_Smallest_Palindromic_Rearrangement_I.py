"""
LeetCode 3517 - Smallest Palindromic Rearrangement I

Difficulty: Medium

Topics:
- String
- Hash Map

Time Complexity: O(n + k log k)

n = length of the string
k = number of distinct characters (maximum 26)

Space Complexity: O(n)

=============================================================
Explanation
=============================================================

The given string is already guaranteed to be a palindrome.

This means every character appears an even number of
times except possibly one character, which appears an
odd number of times.

To obtain the lexicographically smallest palindrome,

1. Build the left half using characters in
   alphabetical order.
2. Place the odd-frequency character (if any)
   in the middle.
3. Mirror the left half to form the right half.

-------------------------------------------------------------

freq = Counter(s)

Count the frequency of every character.

Example

s = "babab"

freq

a → 2

b → 3

-------------------------------------------------------------

left = []

Stores the left half of the palindrome.

-------------------------------------------------------------

mid = ""

Stores the middle character.

Only one character can have an odd frequency.

-------------------------------------------------------------

for ch in sorted(freq)

Traverse every distinct character in
alphabetical order.

Sorting guarantees the smallest
lexicographical palindrome.

-------------------------------------------------------------

left.append(ch * (freq[ch] // 2))

Only half of every character is placed on
the left side.

The remaining half automatically appears
on the right side after reversing.

Example

Character

'a'

Frequency = 4

Left contributes

"aa"

-------------------------------------------------------------

if freq[ch] % 2

If a character appears an odd number of times,

keep one occurrence for the middle.

Example

Frequency = 5

Left

"aa"

Middle

"a"

Right

"aa"

-------------------------------------------------------------

left = "".join(left)

Convert the list into one string.

Example

["aa","bb"]

becomes

"aabb"

-------------------------------------------------------------

return left + mid + left[::-1]

Construct the palindrome.

Left Half

+

Middle Character

+

Reverse of Left Half

=============================================================
Dry Run

Example

s = "daccad"

Frequency

a → 2

c → 2

d → 2

-------------------------------------------------------------

Left Half

"a"

+

"c"

+

"d"

=

"acd"

-------------------------------------------------------------

Middle

None

-------------------------------------------------------------

Right Half

"dca"

-------------------------------------------------------------

Answer

"acddca"

=============================================================
Algorithm

1. Count the frequency of every character.
2. Traverse the characters in sorted order.
3. Add half of every character to the left half.
4. Store the odd-frequency character as the middle.
5. Reverse the left half to form the right half.
6. Return the complete palindrome.
"""

from collections import Counter


class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)

        left = []
        mid = ""

        for ch in sorted(freq):
            left.append(ch * (freq[ch] // 2))

            if freq[ch] % 2:
                mid = ch

        left = "".join(left)

        return left + mid + left[::-1]