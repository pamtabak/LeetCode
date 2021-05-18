# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def get_number_from_linked_list(self, l: ListNode):
        l_number_list = []
        while (l.next != None):
            l_number_list = [str(l.val)] + l_number_list
            l = l.next
        l_number_list = [str(l.val)] + l_number_list
        return int("".join(l_number_list))

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_number = self.get_number_from_linked_list(l1)
        l2_number = self.get_number_from_linked_list(l2)
        sum_l1_l2 = str(l1_number + l2_number)
        current_node: ListNode = ListNode(sum_l1_l2[0])
        for i in range(1, len(sum_l1_l2)):
            next_node: ListNode = ListNode(sum_l1_l2[i], current_node)
            current_node = next_node
        return current_node
