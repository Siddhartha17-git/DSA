"""
LeetCode 921 - Minimum Add to Make Parentheses Valid

Difficulty: Medium

Topics:
- Stack

Time Complexity: O(n)

Space Complexity: O(n)

=============================================================
Explanation
=============================================================

The idea is to use a stack to keep track of unmatched
parentheses.

Whenever we find a matching pair '()',
we remove it from the stack.

At the end, every remaining parenthesis in the stack
must be inserted with its matching pair.

Therefore,

Answer = Number of unmatched parentheses.

-------------------------------------------------------------

stack = []

The stack stores unmatched parentheses.

Initially it is empty.

-------------------------------------------------------------

for i in s

Traverse every character of the string.

-------------------------------------------------------------

if i == "("

An opening bracket cannot be matched immediately.

Push it onto the stack.

Example

Input

"(()"

Stack

(

((

-------------------------------------------------------------

else

Current character is ')'.

Now two cases are possible.

-------------------------------------------------------------

if stack and stack[-1] == "("

A matching opening bracket exists.

Current pair

()

is valid.

Remove the opening bracket from the stack.

Example

Stack

(

Current Character

)

Pop

Stack becomes empty.

-------------------------------------------------------------

else

No matching '(' exists.

So this ')' is unmatched.

Push it onto the stack.

Example

Input

")("

After first ')'

Stack

)

-------------------------------------------------------------

return len(stack)

After processing the entire string,

every element left in the stack is unmatched.

Each unmatched parenthesis requires exactly one insertion.

Hence,

Minimum insertions = length of the stack.

=============================================================
Dry Run

Example

s = "())"

Stack

(

()

)

After processing

Stack

)

Answer = 1

-------------------------------------------------------------

Example

s = "((("

Stack

(

((

(((

No closing brackets exist.

Answer = 3

=============================================================
Algorithm

1. Create an empty stack.
2. Traverse every character.
3. Push every '(' onto the stack.
4. For every ')':
      • If a matching '(' exists, remove it.
      • Otherwise, push ')'.
5. Return the number of unmatched parentheses left in the stack.
"""

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for i in s:
            if i == "(":
                stack.append(i)
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(i)

        return len(stack)