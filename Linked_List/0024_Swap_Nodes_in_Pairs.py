"""
LeetCode 24 - Swap Nodes in Pairs

Difficulty: Medium

Topics:
- Linked List

Time Complexity: O(n)

Space Complexity: O(1)

=============================================================
Explanation
=============================================================

The idea is to swap every two adjacent nodes by changing
their links instead of swapping their values.

To make swapping the head node easier, we create a dummy node
that points to the original head.

-------------------------------------------------------------

dummy = ListNode(0)
dummy.next = head

The dummy node acts as a node before the head.

Example:

dummy -> 1 -> 2 -> 3 -> 4

This avoids handling the first pair as a special case.

-------------------------------------------------------------

prev = dummy

prev always points to the node before the current pair.

Initially,

prev

↓

dummy -> 1 -> 2 -> 3 -> 4

-------------------------------------------------------------

while prev.next and prev.next.next:

A pair exists only if there are at least two nodes.

Continue swapping while two adjacent nodes are available.

-------------------------------------------------------------

first = prev.next
second = first.next

Store references to the two nodes that need to be swapped.

Example:

dummy -> 1 -> 2 -> 3 -> 4

first = 1
second = 2

-------------------------------------------------------------

first.next = second.next

Detach the first node from the pair.

Before

1 -> 2 -> 3

After

1 -> 3

-------------------------------------------------------------

second.next = first

Place the second node before the first node.

Now,

2 -> 1 -> 3

-------------------------------------------------------------

prev.next = second

Connect the previous part of the list to the swapped pair.

The list becomes

dummy -> 2 -> 1 -> 3 -> 4

-------------------------------------------------------------

prev = first

After swapping,

first becomes the second node of the pair.

Move prev to first so it is ready for the next pair.

Example

dummy -> 2 -> 1 -> 3 -> 4

               ↑
             prev

Next pair:

3 -> 4

=============================================================

Dry Run

Input:

1 -> 2 -> 3 -> 4

Initially

dummy -> 1 -> 2 -> 3 -> 4

First swap

dummy -> 2 -> 1 -> 3 -> 4

Second swap

dummy -> 2 -> 1 -> 4 -> 3

Return

2 -> 1 -> 4 -> 3

=============================================================

Algorithm

1. Create a dummy node before the head.
2. Let prev point to the dummy node.
3. While two nodes are available:
      • Store the first and second nodes.
      • Change the links to swap them.
      • Connect the swapped pair back to the list.
      • Move prev to the end of the swapped pair.
4. Return dummy.next as the new head.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            first.next = second.next
            second.next = first
            prev.next = second

            prev = first

        return dummy.next