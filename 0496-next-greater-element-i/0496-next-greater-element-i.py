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
        final=[]      
        for i in range(len(nums1)):
             for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    final.append(result[j])
                    break
        return final            
