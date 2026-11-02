class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = int(matrix[i][j])

        for i in range(len(matrix[0])):
            s = 0
            for j in range(len(matrix)):
                s += matrix[j][i]
                if(matrix[j][i] == 0): s = 0
                matrix[j][i] = s
            
        ans = float('-inf')
        for i in range(len(matrix)):
            stack = []
            for j in range(len(matrix[i])):
                pse = 0
                while(len(stack)>0 and matrix[i][stack[-1]] > matrix[i][j]):
                    element = matrix[i][stack.pop()]
                    nse = j
                    if(len(stack) == 0): pse = -1
                    else: pse = stack[-1]
                    ans = max(ans, element*(nse-pse-1))
                stack.append(j)
            while(len(stack) != 0):
                element = matrix[i][stack.pop()]
                nse = len(matrix[0])
                pse = -1 if(len(stack)==0) else stack[-1]
                ans = max(ans, element*(nse-pse-1))
        return ans