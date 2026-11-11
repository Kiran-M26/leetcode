class Solution(object):
    def calculateScore(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        ab, bb = 0, 0
        while(a>0):
            if(a%2 == 1): ab += 1
            a /= 2
        while(b>0):
            if(b%2 == 1): bb += 1
            b /= 2
        return ab*bb if(ab >= bb) else bb/ab