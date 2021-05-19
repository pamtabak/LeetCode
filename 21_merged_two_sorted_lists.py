# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (l1 == None):
            return l2
        if (l2 == None):
            return l1

        # it means both lists have nodes
        sortedList: ListNode = ListNode(0)
        result = sortedList  # head

        while (l1 != None and l2 != None):
            if (l1.val < l2.val):
                result.next = l1
                l1 = l1.next
            else:
                result.next = l2
                l2 = l2.next
            result = result.next
        result.next = l1 or l2
        return sortedList.next  # we created a head that doesnt exist, so we return the next
