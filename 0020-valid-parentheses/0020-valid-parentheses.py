class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ans = []
        for i in s:
            if(len(ans) == 0): ans.append(i)
            elif(ans[-1]=="(" and i==")"): ans.pop()
            elif(ans[-1]=="{" and i=="}"): ans.pop()
            elif(ans[-1]=="[" and i=="]"): ans.pop()
            else: ans.append(i)
        return True if(len(ans)==0) else False