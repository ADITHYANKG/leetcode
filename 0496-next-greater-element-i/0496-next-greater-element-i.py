class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        def great(x,k):
            for i in range(k,len(nums2)):
                if nums2[i]>x:
                    return nums2[i]
            return -1

        res=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    res.append(great(nums2[j],j))
        return res