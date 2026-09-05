class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp = []
        for i in nums: temp.append(i)
        temp.sort()
        l, r = 0, len(temp)-1
        while(l<r):
            s = temp[l]+temp[r]
            if(s == target): break
            elif(s < target): l += 1
            else: r -= 1
        ans = []
        for i in range(len(nums)):
            if(len(ans) == 2): break
            elif((nums[i] == temp[l]) or (nums[i] == temp[r])): ans.append(i)
        return ans
