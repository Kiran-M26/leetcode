class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num = []
        while(True):
            new_num = 0
            if n in num: return False
            num.append(n)
            while(n>0):
                l = n%10
                new_num += l**2
                n = int(n/10)
            if(new_num == 1): return True
            n = new_num 
        return False