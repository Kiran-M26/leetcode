class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        ans = []
        f, l = strs[0], strs[-1]
        for i in range(min(len(f), len(l))):
            if(f[i] == l[i]): ans.append(f[i])
            else: break
        return "".join(ans)