# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def checkIfFinished (self, lists):
        for lst in lists:
            if (lst != None):
                return False
        return True
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if (len(lists) == 0):
            return None
        
        result = []
        last_number = -1000000
        while (not self.checkIfFinished(lists)):
            smallestNumber = 1000000
            index = -1
            for i in range(0, len(lists)):
                node = lists[i]
                if (node == None):
                    #print(lists)
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
            result.append(smallestNumber)
            lists[index] = lists[index].next
            if (lists[index] == None):
                del lists[index]
        if (len(result) == 0):
            return None
        #we now need to convert the list to a linked-list
        linkedList: ListNode = ListNode(result[-1])
        for i in range(len(result) - 2, -1, -1):
            linkedList: ListNode = ListNode(result[i], linkedList)
        return linkedList