class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in nums1: 
            if i in ans: continue
            else: ans.append(i)
        for i in nums2: 
            if i in ans: continue
            else: ans.append(i)
        for i in nums3: 
            if i in ans: continue
            else: ans.append(i)
        temp = []
        for i in ans:
            if (i in nums1 and i in nums2) or (i in nums2 and i in nums3) or (i in nums3 and i in nums1): temp.append(i)
        return temp