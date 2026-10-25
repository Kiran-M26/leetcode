class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        ans = 0
        al = list(allowed)
        for i in range(len(words)):
            a = 0
            for j in words[i]:
                if j not in al: a += 1
            if(a == 0): ans+=1
        return ans