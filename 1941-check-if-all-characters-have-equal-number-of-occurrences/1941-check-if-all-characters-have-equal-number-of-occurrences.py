class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        freq = {}
        for i in s:
            if i in freq: freq[i] += 1
            else: freq[i] = 1
        s = []
        for i, j in freq.items():
            s.append(j)
        return True if(len(set(s)) == 1) else False