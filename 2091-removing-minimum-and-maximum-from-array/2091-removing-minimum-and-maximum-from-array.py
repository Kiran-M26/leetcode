class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s, l = 0, 0
        for i in range(len(nums)):
            if(nums[i] > nums[l]): l = i
            if(nums[i] < nums[s]): s = i
        left, right = min(l, s), max(l, s)
        left_remove, right_remove, both_remove = right+1, len(nums)-left, (left+1)+(len(nums)-right)
        return min(left_remove, right_remove, both_remove)