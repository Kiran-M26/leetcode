class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        es = 0
        for i in nums: es += i
        ds = 0
        for i in nums:
            if(i<10): ds += i
            else:
                while(i>0):
                    ds += i%10
                    i //= 10
        return abs(es-ds)