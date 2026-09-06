class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = []
        for i in range(len(s)):
            if(s[i] == "*"): ans.pop()
            else: ans.append(s[i])
        return "".join(ans)