"""
LeetCode 1189 - Maximum Number of Balloons

Difficulty: Easy

Topics:
- Hash Map
- String
- Counting

Time Complexity: O(n)
Space Complexity: O(1)

=============================================================
Explanation
=============================================================

We only care about the characters needed to form the word:

balloon

Required characters:
b -> 1
a -> 1
l -> 2
o -> 2
n -> 1

-------------------------------------------------------------

letters = {}

Stores the frequency of only the required characters.

letters["b"]
letters["a"]
letters["l"]
letters["o"]
letters["n"]

-------------------------------------------------------------

for i in text:

Traverse every character in the given string.

If the character is one of:

'b', 'a', 'l', 'o', 'n'

increase its frequency.

-------------------------------------------------------------

letters["l"] //= 2
letters["o"] //= 2

The word "balloon" contains:

l -> 2 times
o -> 2 times

For example,

If text contains:

l = 5

Then we can use only:

5 // 2 = 2 complete pairs of 'l'

Similarly,

o = 7

7 // 2 = 3 complete pairs of 'o'

-------------------------------------------------------------

for j in "balon":

The maximum number of "balloon" words depends on the
character that appears the fewest number of times.

Example:

b = 4
a = 3
l = 2
o = 5
n = 3

Answer = min(4, 3, 2, 5, 3)

which is 2.

=============================================================

Algorithm

1. Count the frequency of only the required characters.
2. Divide the count of 'l' and 'o' by 2 because each
   balloon needs two of them.
3. Find the minimum frequency among
   b, a, l, o and n.
4. Return that minimum value.
"""

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = {}
        letters["b"] = 0
        letters["a"] = 0
        letters["l"] = 0
        letters["o"] = 0
        letters["n"] = 0

        for i in text:
            if i in "balon":
                letters[i] += 1

        min_count = float("+inf")

        letters["l"] //= 2
        letters["o"] //= 2

        for j in "balon":
            min_count = min(min_count, letters[j])

        return min_count