class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        l, h = 1, max(nums)
        while(l<=h):
            m = (l+h)//2
            s = 0
            for i in nums:
                k = (i+m-1)//m
                s += k
            if(s<=threshold): h = m-1
            else: l = m+1
        return l