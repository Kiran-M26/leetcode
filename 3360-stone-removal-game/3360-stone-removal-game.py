class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return True if ((n>9)and(n<19)) or ((n>26)and(n<34)) or ((n>39)and(n<45)) or ((n>48)and(n<52)) or ((n>53)and(n<55)) else False