class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        n = len(nums)
        for i in range(len(nums)):
            if(n%(i+1) == 0): ans += nums[i]*nums[i]
        return ans