class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        sl = s.split()
        if(len(pattern) != len(sl)): return False
        d = {}
        for letter, word in zip(pattern, sl):
            if letter in d:
                if(d[letter] != word): return False
            else:
                d[letter] = word
        return len(set(d.values())) == len(d)