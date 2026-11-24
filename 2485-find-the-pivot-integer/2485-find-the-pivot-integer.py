class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        ls, rs = [], []
        l = 0
        for i in range(1, n+1):
            l += i
            ls.append(l)
        m = ls[len(ls)-1]
        rs.append(m)
        for i in range(2, n+1):
            m -= (i-1)
            rs.append(m)
        ans = -1
        for i in range(len(ls)):
            if(ls[i] == rs[i]):
                ans = i+1
                break
        return ans