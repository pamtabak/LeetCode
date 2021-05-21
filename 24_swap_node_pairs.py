# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        result = head
        if result is None or result.next is None:
            return result

        # we only need to change the nodes' values. so we switch the current node val with the next node val, than skip two nodes
        while (result is not None and result.next is not None):
            val = result.val
            result.val = result.next.val
            result.next.val = val
            result = result.next.next

        return head
