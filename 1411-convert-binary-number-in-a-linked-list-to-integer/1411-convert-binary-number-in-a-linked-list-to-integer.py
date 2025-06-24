# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        curr=head
        res=""
        while curr is not None:
            res+=str(curr.val)
            curr=curr.next
            
        fr=0    
        for i in range(len(res)):
            fr+=int(res[i])*(2**(len(res)-i-1))
        return fr




        