class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if(n<1000) else n-999
        