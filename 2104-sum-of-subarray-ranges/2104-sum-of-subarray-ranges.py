class Solution(object):
    def Sum_Max(self, nums):
        nge, pgee = [0]*len(nums), [0]*len(nums)
        nstack, pstack = [], []
        for i in range(len(nums)-1, -1, -1):
            while(len(nstack)>0 and nums[nstack[-1]]<nums[i]): nstack.pop()
            if(len(nstack) == 0): nge[i] = len(nums)
            else: nge[i] = nstack[-1]
            nstack.append(i)
        
        for i in range(len(nums)):
            while(len(pstack)>0 and nums[pstack[-1]]<=nums[i]): pstack.pop()
            if(len(pstack) == 0): pgee[i] = -1
            else: pgee[i] = pstack[-1]
            pstack.append(i)

        total = 0
        for i in range(len(nums)):
            left, right = i-pgee[i], nge[i]-i
            total += (nums[i]*left*right)

        return total

    def Sum_Min(self, nums):
        nse, psee = [0]*len(nums), [0]*len(nums)
        nstack, pstack = [], []
        for i in range(len(nums)-1, -1, -1):
            while(len(nstack)>0 and nums[nstack[-1]]>nums[i]): nstack.pop()
            if(len(nstack)==0): nse[i] = len(nums)
            else: nse[i] = nstack[-1]
            nstack.append(i)

        for i in range(len(nums)):
            while(len(pstack)>0 and nums[pstack[-1]]>=nums[i]): pstack.pop()
            if(len(pstack) == 0): psee[i] = -1
            else: psee[i] = pstack[-1]
            pstack.append(i)
        
        total = 0
        for i in range(len(nums)):
            left, right = i-psee[i], nse[i]-i
            total += (nums[i]*left*right)

        return total 

    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.Sum_Max(nums)- self.Sum_Min(nums)