class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        sp = s.split(" ")
        so = {}
        for i in range(len(sp)):
            so[int(sp[i][-1])] = sp[i][:-1]
        ans = [0]*len(sp)
        for i, j in so.items():
            ans[i-1] = j
        return " ".join(ans)