"""
LeetCode 2409 - Count Days Spent Together

Difficulty: Easy

Topics:
- Math
- Arrays
- Date Conversion

Time Complexity: O(1)
Space Complexity: O(1)

Approach:
Convert each date from MM-DD format into its day number in the year.

The finddate() function adds the days of all previous months to
the current day.

Then calculate the overlapping interval:
    start = max(alice1, bob1)
    end = min(alice2, bob2)

If start > end, there is no overlap, so return 0.
Otherwise, return end - start + 1 because both dates are inclusive.

Dry Run:
arriveAlice = "08-15", leaveAlice = "08-18"
arriveBob = "08-16", leaveBob = "08-19"

Day numbers:
    alice1 = 227, alice2 = 230
    bob1 = 228, bob2 = 231

start = max(227, 228) = 228
end = min(230, 231) = 230

Answer = 230 - 228 + 1 = 3

Algorithm:
1. Store the number of days in each month.
2. Convert all four dates into day numbers.
3. Find the later arrival and earlier departure.
4. If start > end, return 0.
5. Otherwise, return end - start + 1.
"""

class Solution:
    def countDaysTogether(
        self,
        arriveAlice: str,
        leaveAlice: str,
        arriveBob: str,
        leaveBob: str
    ) -> int:

        monthdays = [31, 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]

        def finddate(s):
            month = int(s[0:2])
            day = int(s[3:5])
            value = 0

            for i in range(month - 1):
                value += monthdays[i]

            value += day
            return value

        alice1 = finddate(arriveAlice)
        alice2 = finddate(leaveAlice)
        bob1 = finddate(arriveBob)
        bob2 = finddate(leaveBob)

        start = max(alice1, bob1)
        end = min(alice2, bob2)

        if start > end:
            return 0

        return end - start + 1