# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        prevA = list1
        for _ in range(a - 1):
            prevA = prevA.next

        # Step 2: Find node after 'b'
        curr = prevA
        for _ in range(b - a + 2):
            curr = curr.next

        # Step 3: Connect prevA to head of list2
        prevA.next = list2

        # Step 4: Go to end of list2
        tail = list2
        while tail.next:
            tail = tail.next

        # Step 5: Connect tail of list2 to node after b
        tail.next = curr

        return list1
        