class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        ans = []
        nums = []
        for i in range(1, n+1):
            if(nums == target): return ans
            ans.append("Push")
            nums.append(i)
            if i not in target:
                ans.append("Pop")
                nums.pop()
        return ans