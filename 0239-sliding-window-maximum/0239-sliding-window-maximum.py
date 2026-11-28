from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        queue = deque()
        for i in range(len(nums)):
            if(len(queue)>0 and queue[0]<=i-k): queue.popleft()
            while((len(queue)>0) and (nums[queue[-1]]<=nums[i])): queue.pop()
            queue.append(i)
            if(i>=k-1): ans.append(nums[queue[0]])
        return ans