"""
LeetCode 1221 - Split a String in Balanced Strings

Difficulty: Easy

Topics:
- Greedy
- String

Time Complexity: O(n)

The string is traversed once.

Space Complexity: O(1)

Only two counters are maintained.

=============================================================
Explanation
=============================================================

A balanced string contains the same number of 'L' and 'R'.

The goal is to split the given balanced string into the
maximum possible number of balanced substrings.

The key observation is:

Whenever the number of L's becomes equal to the number
of R's, the current substring is balanced.

Therefore, we can immediately count a balanced substring
and continue from the next character.

This is a greedy approach because we make the split at
the earliest possible position.

-------------------------------------------------------------

dic = {"L": 0, "R": 0}

Stores the number of L and R characters seen so far.

-------------------------------------------------------------

output = 0

Stores the number of balanced substrings found.

-------------------------------------------------------------

for i in s:

Process every character.

-------------------------------------------------------------

dic[i] += 1

Increase the count of the current character.

-------------------------------------------------------------

if dic["L"] == dic["R"]:

The number of L's and R's is equal.

Therefore, the current substring is balanced.

Increment the answer.

-------------------------------------------------------------

output += 1

Then continue processing the remaining characters.

=============================================================
Dry Run

Example:

s = "RLRRLLRLRL"

Start:

L = 0
R = 0
answer = 0

-------------------------------------------------------------

R

L = 0
R = 1

Not balanced.

-------------------------------------------------------------

L

L = 1
R = 1

Balanced.

answer = 1

-------------------------------------------------------------

R

L = 1
R = 2

Not balanced.

-------------------------------------------------------------

R

L = 1
R = 3

Not balanced.

-------------------------------------------------------------

L

L = 2
R = 3

Not balanced.

-------------------------------------------------------------

L

L = 3
R = 3

Balanced.

answer = 2

Continue similarly.

Final answer:

4

=============================================================
Why Greedy Works

Suppose the current substring becomes balanced.

There is no benefit in extending the substring further
before making the split.

If we split immediately, we leave the remaining characters
available to potentially form another balanced substring.

Therefore, taking every earliest possible balanced prefix
maximizes the total number of balanced substrings.

=============================================================
Algorithm

1. Keep counts of L and R.
2. Traverse the string.
3. Increment the count of the current character.
4. Whenever L == R, increment the answer.
5. Return the answer.
"""

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        dic = {"L": 0, "R": 0}
        output = 0

        for i in s:
            dic[i] += 1

            if dic["L"] == dic["R"]:
                output += 1

        return output