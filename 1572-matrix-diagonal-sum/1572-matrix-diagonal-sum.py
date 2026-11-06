class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in range(len(mat)):
            ans += mat[i][i]
            ans += mat[i][len(mat)-1-i]
        if(len(mat)%2 == 1):
            d = len(mat)//2
            ans -= mat[d][d]
        return ans