class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n=len(nums2)
        result=[-1]*n
        stack=[]
        for i in range(n):
            while stack and nums2[i]>nums2[stack[-1]]:
                index=stack.pop()
                result[index]=nums2[i]
            stack.append(i)  
        next_map={nums2[i]:result[i] for i in range(n)}

        return [next_map[x] for x in nums1]         
