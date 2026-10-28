class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        b = bin(num)[2:]
        ans = ""
        for i in b:
            if(i == "0"): ans+="1"
            else: ans+="0"
        return int(ans, 2)