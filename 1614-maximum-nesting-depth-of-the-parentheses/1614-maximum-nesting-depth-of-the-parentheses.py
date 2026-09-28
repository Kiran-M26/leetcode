class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        stack = []
        for i in s:
            if(i == "("):
                stack.append(i)
            elif(i == ")"):
                stack.pop()
            cnt = max(cnt, len(stack))
        return cnt