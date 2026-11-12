class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 1
        icnt = 1
        dcnt = 1
        for i in range(1, len(nums)):
            if(nums[i] > nums[i-1]): icnt += 1
            else: icnt = 1
            if(nums[i-1] > nums[i]): dcnt += 1
            else: dcnt = 1
            ans = max(ans, max(icnt, dcnt))
        return ans
        