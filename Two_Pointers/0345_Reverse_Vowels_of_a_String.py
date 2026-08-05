"""
LeetCode 345 - Reverse Vowels of a String

Difficulty: Easy

Topics:
- Two Pointers
- String

Time Complexity: O(n)

Each pointer traverses the string at most once.

Space Complexity: O(n)

A list of characters is created since strings are immutable.

=============================================================
Explanation
=============================================================

The goal is to reverse only the vowels while keeping
all other characters in their original positions.

Since Python strings are immutable,

first convert the string into a list.

Then use two pointers.

Left pointer searches for the next vowel.

Right pointer searches for the previous vowel.

When both pointers point to vowels,

swap them.

=============================================================
Initialization

-------------------------------------------------------------

lis = list(s)

Convert the string into a list so characters can
be modified.

-------------------------------------------------------------

vowel = "aeiouAEIOU"

Contains every lowercase and uppercase vowel.

Membership checking is done using

character in vowel

-------------------------------------------------------------

i = 0

Left pointer.

-------------------------------------------------------------

j = len(s) - 1

Right pointer.

=============================================================
Main Loop

-------------------------------------------------------------

while i < j

Continue until both pointers meet.

-------------------------------------------------------------

Case 1

if lis[i] in vowel and lis[j] in vowel

Both pointers point to vowels.

Swap them.

Move both pointers.

-------------------------------------------------------------

Example

A b c e

^

      ^

Swap

e b c A

-------------------------------------------------------------

Case 2

elif lis[i] not in vowel and lis[j] in vowel

Left is not a vowel.

Move the left pointer.

-------------------------------------------------------------

Case 3

elif lis[i] in vowel and lis[j] not in vowel

Right is not a vowel.

Move the right pointer.

-------------------------------------------------------------

Case 4

else

Neither character is a vowel.

Move both pointers.

=============================================================
Dry Run

Example

s = "IceCreAm"

Initial

I c e C r e A m

i               j

-------------------------

Right is not vowel

Move j

-------------------------

I and A

Swap

A c e C r e I m

Move both

-------------------------

e and e

Swap

No change

-------------------------

Pointers meet

Answer

"AceCreIm"

=============================================================
Algorithm

1. Convert the string into a list.
2. Initialize two pointers.
3. Move the left pointer until a vowel is found.
4. Move the right pointer until a vowel is found.
5. Swap both vowels.
6. Continue until the pointers meet.
7. Convert the list back into a string.
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        lis = list(s)

        vowel = "aeiouAEIOU"

        i = 0
        j = len(s) - 1

        while i < j:

            if lis[i] in vowel and lis[j] in vowel:
                lis[i], lis[j] = lis[j], lis[i]
                i += 1
                j -= 1

            elif lis[i] not in vowel and lis[j] in vowel:
                i += 1

            elif lis[i] in vowel and lis[j] not in vowel:
                j -= 1

            else:
                i += 1
                j -= 1

        return "".join(lis)