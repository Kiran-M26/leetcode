class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return True if ("a" in s) or ("e" in s) or ("i" in s) or ("o" in s) or ("u" in s) else False