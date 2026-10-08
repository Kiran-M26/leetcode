class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        for _ in range(n):
            ans.append([0]*n)
        l, r, t, b = 0, n-1, 0, n-1
        ele = 1
        while(l<=r and t<=b):
            for i in range(l, r+1):
                ans[t][i] = ele
                ele += 1
            t += 1
            for i in range(t, b+1):
                ans[i][r] = ele
                ele += 1
            r -= 1
            for i in range(r, l-1, -1):
                ans[b][i] = ele
                ele += 1
            b -= 1
            for i in range(b, t-1, -1):
                ans[i][l] = ele
                ele += 1
            l += 1
        return ans