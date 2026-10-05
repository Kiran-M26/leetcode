class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        temp = 0
        for i in s:
            if(i != " "): temp += 1
            elif(temp>0 and i==" "):
                cnt += 1
                temp = 0
        if(temp>0): cnt += 1
        return cnt