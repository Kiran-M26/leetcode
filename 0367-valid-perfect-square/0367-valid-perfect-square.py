class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l, h = 1, num/2 + 1
        while(l <= h):
            m = (l+h)//2
            s = m*m
            if(s == num): return True
            elif(s < num): l = m+1
            else: h = m-1
        return False