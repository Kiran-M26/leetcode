class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        i, inc = 0, 1
        while(i<n):
            ans += 1
            inc += 1
            i += inc
        return ans
