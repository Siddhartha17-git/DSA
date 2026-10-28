"""
LeetCode 1358 - Number of Substrings Containing All Three Characters

Difficulty: Medium

Topics:
- Sliding Window
- String

Time Complexity: O(n)
Space Complexity: O(1)

=============================================================
Explanation
=============================================================

count = [0] * 3
----------------
Stores the frequency of each character in the current window.

count[0] -> frequency of 'a'
count[1] -> frequency of 'b'
count[2] -> frequency of 'c'

We convert characters into indices using:

ord(s[i]) - ord('a')

'a' -> 0
'b' -> 1
'c' -> 2

-------------------------------------------------------------

for right in range(n):
    count[ord(s[right]) - ord('a')] += 1

Move the right pointer one step at a time and include the
current character in the sliding window.

-------------------------------------------------------------

while count[0] > 0 and count[1] > 0 and count[2] > 0:

This means the current window contains at least one
'a', one 'b', and one 'c'.

So the current window is valid.

-------------------------------------------------------------

ans += n - right

Suppose

s = "abcabc"

Current window = "abc"
right = 2
n = 6

Every substring starting at 'left' and ending at:

2 -> "abc"
3 -> "abca"
4 -> "abcab"
5 -> "abcabc"

will also contain a, b and c.

Therefore,

Number of valid substrings = n - right

Instead of checking each one individually, we count them all
at once.

-------------------------------------------------------------

count[ord(s[left]) - ord('a')] -= 1
left += 1

After counting all valid substrings, move the left pointer.

Before moving left, remove its character from the frequency
array because it is no longer inside the window.

Continue shrinking until the window becomes invalid.

Then move the right pointer again.

=============================================================

Algorithm

1. Expand the window by moving right.
2. Update the frequency of the current character.
3. If the window contains a, b and c:
      - Add (n - right) to the answer.
      - Remove the left character.
      - Move left.
4. Repeat until the end of the string.
"""

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = [0] * 3
        left = 0
        ans = 0
        n = len(s)

        for right in range(n):
            count[ord(s[right]) - ord('a')] += 1

            while count[0] > 0 and count[1] > 0 and count[2] > 0:
                ans += n - right
                count[ord(s[left]) - ord('a')] -= 1
                left += 1

        return ans