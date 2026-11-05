class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        ans = []
        cp = []
        for i in range(len(s)):
            if(s[i] == c): cp.append(i)
        for i in range(len(s)):
            d = float('inf')
            for j in range(len(cp)):
                d = min(d, abs(cp[j]-i))
            ans.append(d)
        return ans