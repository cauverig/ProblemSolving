"""Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.

Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""


def deleteDuplicates(self, head):
    current = head
    while current:
        while current.next and current.next.val == current.val:
            current.next = current.next.next    # skip duplicated node
        current = current.next  # not duplicate of current node, move to next noce
    return head
