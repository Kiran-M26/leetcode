class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        for i in nums: s += i
        ts = 0
        ans = 0
        for i in range(len(nums)-1):
            s -= nums[i]
            ts += nums[i]
            if(abs(s-ts)%2 == 0): ans += 1
        return ans