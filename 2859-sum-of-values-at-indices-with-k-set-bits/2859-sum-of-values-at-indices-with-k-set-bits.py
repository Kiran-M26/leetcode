class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        for i in range(len(nums)):
            b = 0
            temp = i
            while(i>0):
                bit = i%2
                if(bit == 1): b += 1
                i = int(i/2)
            if(b == k): ans += nums[temp]
        return ans