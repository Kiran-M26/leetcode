class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = [-1]*(len(nums)+1)
        for i in range(len(nums)):
            temp[nums[i]] = 1
        ans = []
        for i in range(1, len(temp)):
            if(temp[i] == -1): ans.append(i)
        return ans