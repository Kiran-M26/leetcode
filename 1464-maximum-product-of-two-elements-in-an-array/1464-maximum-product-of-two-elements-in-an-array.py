class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fl, sl = float("-inf"), float("-inf")
        for i in nums:
            if(i >= fl): 
                sl = fl
                fl = i
            elif(i<fl and i>sl):
                sl = i
        return ((fl-1)*(sl-1))