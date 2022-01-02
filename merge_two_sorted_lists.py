"""You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list."""


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        Starter = ListNode(0)  # Sentinel node
        curr = Starter  # creating a copy of starter node so as to iteratively add splice from input lists

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                temp = list1
                curr.next = temp
                list1 = list1.next
                temp.next = None
            else:
                temp = list2
                curr.next = temp
                list2 = list2.next
                temp.next = None
            curr = curr.next
        # add the remaining nodes of longer list
        if list1 is None:
            curr.next = list2
        else:
            curr.next = list1
        return Starter.next
