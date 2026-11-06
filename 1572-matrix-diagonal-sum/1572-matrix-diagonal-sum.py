class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if(i == j): ans += mat[i][j]
                elif(j+i == len(mat)-1): ans += mat[i][j]
        return ans