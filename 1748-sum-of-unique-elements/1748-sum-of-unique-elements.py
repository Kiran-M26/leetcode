class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for i in nums:
            if i in freq: freq[i] += 1
            else: freq[i] = 1
        ans = 0
        for key, value in freq.items():
            if(value == 1): ans += key
        return ans