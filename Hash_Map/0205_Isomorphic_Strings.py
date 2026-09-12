"""
LeetCode 205 - Isomorphic Strings

Difficulty: Easy

Topics:
- Hash Map
- String

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
Two strings are isomorphic when every character in `s` consistently
maps to exactly one character in `t`, and no two different characters
in `s` map to the same character in `t`.

To enforce this one-to-one relationship, we use two dictionaries:

1. `dic`
   Maps characters from `s` -> `t`.

2. `dic1`
   Maps characters from `t` -> `s`.

For every position i:
- If s[i] has already been mapped, we check that it maps to t[i].
- If t[i] has already been mapped, we check that it maps back to s[i].
- If either mapping contradicts an existing mapping, return False.
- Otherwise, store both mappings.

The two dictionaries are necessary because checking only one direction
would not guarantee a bijection.

Example:
s = "egg", t = "add"

Mapping:
    e -> a
    g -> d

Reverse mapping:
    a -> e
    d -> g

All mappings remain consistent, so the strings are isomorphic.


Dry Run:
s = "paper"
t = "title"

i = 0:
    p -> t
    t -> p

i = 1:
    a -> i
    i -> a

i = 2:
    p already maps to t
    t already maps to p
    consistent

i = 3:
    e -> l
    l -> e

i = 4:
    r -> e
    e -> r

All mappings are consistent.

Return True.


Example of a contradiction:
s = "f11"
t = "b23"

i = 0:
    f -> b
    b -> f

i = 1:
    1 -> 2
    2 -> 1

i = 2:
    1 already maps to 2,
    but t[2] is 3.

Therefore, return False.


Algorithm:
1. Create two empty dictionaries.
2. Iterate through both strings simultaneously using their indices.
3. Check whether the existing s -> t mapping is consistent.
4. Check whether the existing t -> s mapping is consistent.
5. If either mapping is inconsistent, return False.
6. Store both mappings.
7. If the entire string is processed successfully, return True.
"""

class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:

        dic = {}
        dic1 = {}

        for i in range(len(s)):

            if s[i] in dic and t[i] != dic[s[i]]:
                return False

            if t[i] in dic1 and s[i] != dic1[t[i]]:
                return False

            dic[s[i]] = t[i]
            dic1[t[i]] = s[i]

        return True