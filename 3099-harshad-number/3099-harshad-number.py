class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        sod, temp = 0, x
        while(x>0):
            sod += x%10
            x //= 10
        return sod if(temp%sod == 0) else -1