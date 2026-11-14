class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        s = float('inf')
        for i in range(l, r+1):
            win = 0
            ts = float('inf')
            for j in range(i): win += nums[j]
            for j in range(i-1, len(nums)):
                if(j>=i): win += nums[j]-nums[j-i]
                if(win>0 and win<ts): ts = win
            s = min(s, ts)
        if(s == float('inf')): return -1
        return s if(s>0) else -1