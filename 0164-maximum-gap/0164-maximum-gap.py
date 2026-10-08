class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) < 2): return 0
        m = 0
        nums.sort()
        for i in range(len(nums)-1):
            m = max(m, abs(nums[i]-nums[i+1]))
        return m