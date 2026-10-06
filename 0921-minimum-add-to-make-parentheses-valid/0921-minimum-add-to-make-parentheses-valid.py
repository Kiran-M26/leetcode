class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        ocnt = 0
        for i in s:
            if(i == "("):
                ocnt += 1
            elif(ocnt > 0):
                ocnt -= 1
            elif(ocnt == 0):
                cnt += 1
        return cnt+ocnt 