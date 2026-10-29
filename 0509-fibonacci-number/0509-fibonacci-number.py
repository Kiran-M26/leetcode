class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        f, s = 0, 1
        t = 0
        if(n < 1): return 0
        if(n <= 1): return 1
        for i in range(2, n+1):
            t = s
            s += f
            f = t
        return s