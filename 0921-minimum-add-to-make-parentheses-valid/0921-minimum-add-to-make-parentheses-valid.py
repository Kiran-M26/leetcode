class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        cnt = 0
        ocnt = 0
        for i in s:
            if(i == "("): 
                stack.append(i)
                ocnt += 1
            elif(len(stack) > 0):
                stack.pop()
                ocnt -= 1
            elif(len(stack) == 0):
                cnt += 1
        return cnt+ocnt 