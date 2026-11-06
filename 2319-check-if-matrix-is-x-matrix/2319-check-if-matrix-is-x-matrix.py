class Solution(object):
    def checkXMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        ans = True
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(ans == False): return False
                elif((i==j) or (j==len(grid)-1-i)): 
                    if(grid[i][j] == 0):
                        ans = False
                        continue
                elif(grid[i][j] != 0): return False
        return ans