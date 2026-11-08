class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lv, rv = 0, 0
        for i in range(len(s)):
            if s[i] in ["a", "e", "i","o", "u", "A", "E", "I", "O", "U"]:
                if(i < (len(s)+1)/2): lv += 1
                else: rv += 1
        return True if(lv==rv) else False