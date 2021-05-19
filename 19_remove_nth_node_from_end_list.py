# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def simpleAlgorithm(self, head: ListNode, n: int) -> ListNode:
        # we create a temp node to simplify things and add it as head (is really helpful in an empty list)
        tempNode: ListNode = ListNode(0)
        tempNode.next = head

        # now we iterate through the list to discover its length
        node: ListNode = head
        size = 0
        while (node != None):
            size += 1
            node = node.next

        # now what we want to do is remove the n-th node
        size -= n
        node: ListNode = tempNode
        while (size > 0):
            size -= 1
            node = node.next
        node.next = node.next.next  # we now skip the n-th node
        return tempNode.next  # we return the head of the list, removing the temp node

    def singlePassAlgorithm(self, head: ListNode, n: int) -> ListNode:
        # we create a temp node to simplify things and add it as head (is really helpful in an empty list)
        tempNode: ListNode = ListNode(0)
        tempNode.next = head

        firstPointer = tempNode
        secondPointer = tempNode

        # we want the first and the second pointer to be n nodes apart
        for i in range(n+1):
            firstPointer = firstPointer.next

        while (firstPointer != None):
            firstPointer = firstPointer.next
            secondPointer = secondPointer.next

        secondPointer.next = secondPointer.next.next

        return tempNode.next

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        return self.singlePassAlgorithm(head, n)
