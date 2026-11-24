class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if(num == 0): return True
        elif(num%10 == 0): return False
        else: return True