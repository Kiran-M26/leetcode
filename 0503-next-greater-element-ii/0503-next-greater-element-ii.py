class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        ans = [0]*len(nums)
        for i in range(len(nums)-1, -1, -1): stack.append(nums[i])
        for i in range(len(nums)-1, -1, -1):
            while(len(stack) > 0 and stack[-1] <= nums[i]): stack.pop()
            if(len(stack) == 0): ans[i] = -1
            else: ans[i] = stack[-1]
            stack.append(nums[i])
        return ans