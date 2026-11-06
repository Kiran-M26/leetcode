class Solution(object):
    def peakValleyDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        psum, vsum = 0, 0
        for i in range(1, len(nums)-1):
            if(nums[i]>nums[i-1] and nums[i]>nums[i+1]): psum += nums[i]
            elif(nums[i]<nums[i-1] and nums[i]<nums[i+1]): vsum += nums[i]
        return psum-vsum