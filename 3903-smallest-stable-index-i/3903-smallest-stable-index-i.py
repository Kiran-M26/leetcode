class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxi = nums[0]
        for i in range(len(nums)):
            if(nums[i] > maxi): maxi = nums[i]
            mini = nums[i]
            for j in range(i, len(nums)):
                if(nums[j] < mini): mini = nums[j]
            instability = maxi-mini
            if(instability <= k): return i
        return -1
