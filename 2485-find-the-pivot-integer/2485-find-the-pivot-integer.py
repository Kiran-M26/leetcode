class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = n*(n+1)//2
        ans = -1
        for i in range(1, n+1):
            ls = total - i*(i+1)//2 + i
            rs = total - ls + i
            if(ls == rs):
                ans = i
                break
        return ans