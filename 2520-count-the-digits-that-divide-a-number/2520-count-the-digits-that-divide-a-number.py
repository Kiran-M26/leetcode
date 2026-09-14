class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        temp = num
        while(temp>0):
            l = temp%10
            if(num%l == 0):
                count += 1
            temp //= 10
        return count