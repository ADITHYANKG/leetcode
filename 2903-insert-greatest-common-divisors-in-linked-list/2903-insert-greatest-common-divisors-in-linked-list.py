# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from fractions import gcd
class Solution(object):
    
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        current = head
        while current and current.next:
            gcd_value = gcd(current.val, current.next.val)
            new_node = ListNode(gcd_value)
            # Insert the new node
            new_node.next = current.next
            current.next = new_node
            # Move to the next original node
            current = new_node.next
        return head
        


        