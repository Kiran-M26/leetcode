class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bp = -1
        for i in range(len(s)): 
            if(s[i] == "b"): 
                bp = i
                break
        for i in range(i+1, len(s)):
            if(s[i] == "a"): return False
        return True