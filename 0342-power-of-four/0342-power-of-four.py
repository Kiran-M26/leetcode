class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while(n>1):
            if(n%4 != 0): return False
            n//=4
        return True if(n == 1) else False