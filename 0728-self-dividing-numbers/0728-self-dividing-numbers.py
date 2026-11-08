class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = []
        for i in range(left, right+1):
            temp = i
            while(i>0):
                l = i%10
                if(l==0 or temp%l != 0): break
                i //= 10
            if(i==0): ans.append(temp)
        return ans