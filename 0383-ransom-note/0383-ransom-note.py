class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        freq = {}
        for i in magazine:
            if i in freq: freq[i] += 1
            else: freq[i] = 1
        for i in ransomNote:
            if i in freq: 
                if freq[i] == 0: return False
                else: freq[i] -= 1
            else:
                return False
        return True