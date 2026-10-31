class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        ans = float('-inf')
        for i in range(len(heights)):
            while(len(stack) != 0 and heights[stack[-1]]>heights[i]):
                element = heights[stack.pop()]
                nse = i
                pse = -1 if(len(stack) == 0) else stack[-1]
                ans = max(ans, element*(nse-pse-1))
            stack.append(i)

        while(len(stack) != 0):
            element = heights[stack.pop()]
            nse = len(heights)
            pse = -1 if(len(stack) == 0) else stack[-1]
            ans = max(ans, element*(nse-pse-1))

        return ans