class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersection = []
        for i in nums1:
            if i not in intersection and  i in nums2: intersection.append(i)
        for i in nums2: 
            if i not in intersection and i in nums1: intersection.append(i)
        return intersection