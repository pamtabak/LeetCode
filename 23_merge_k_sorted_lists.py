# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def checkIfFinished(self, lists):
        for lst in lists:
            if (lst != None):
                return False
        return True

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if (len(lists) == 0):
            return None

        head: ListNode = ListNode(0)
        result = head

        last_number = -1000000
        while (not self.checkIfFinished(lists)):
            smallestNumber = 1000000
            index = -1
            for i in range(0, len(lists)):
                node = lists[i]
                if (node == None):
                    continue
                value = node.val
                if (value == last_number):
                    smallestNumber = value
                    index = i
                    break
                if (value <= smallestNumber):
                    smallestNumber = value
                    index = i
            last_number = smallestNumber
            result.next = ListNode(smallestNumber)
            result = result.next
            lists[index] = lists[index].next
            if (lists[index] == None):
                del lists[index]
        return head.next
