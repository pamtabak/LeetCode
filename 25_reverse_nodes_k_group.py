# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # this is a simple solution that solves the problem, but using lots of extra memory space (since we create 2 lists of ints and a new ListNode too)
    def simpleSolution(self, head: ListNode, k: int) -> ListNode:
        listValues = []
        while (head != None):
            listValues.append(head.val)
            head = head.next

        if (len(listValues) == 0):
            return None

        # shift values
        newList = []
        i = 0
        while (i < len(listValues)):
            if (len(listValues) - i < k):
                newList.append(listValues[i])
                i += 1
                continue
            kList = listValues[i:k+i]
            kList.reverse()
            for element in kList:
                newList.append(element)
            i += k

        result = ListNode(0)
        lastNode = None
        for i in range(len(newList) - 1, -1, -1):
            result = ListNode(newList[i], lastNode)
            lastNode = result
        return result

    def elegantSolution(self, head: ListNode, k: int) -> ListNode:
        # we first count how many nodes there are
        length = 0
        result = head
        while (result != None):
            length += 1
            result = result.next

        listNode: ListNode = ListNode(0)
        listNode.next = head

        iterator = 0
        result = listNode.next
        while (iterator < length):
            if (length - iterator >= k):
                # we know there are at least k nodes in the sequence that need to be changed
                vals = []
                currentNode = result
                for i in range(k):
                    vals.append(currentNode.val)
                    currentNode = currentNode.next
                for i in range(k):
                    result.val = vals[k - i - 1]
                    result = result.next
                iterator += k
            else:
                result = result.next
                iterator += 1

        return listNode.next

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        return self.elegantSolution(head, k)
