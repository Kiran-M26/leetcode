class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        h = []
        for i in s:
            if i in h: return i
            else: h.append(i)
        return -1