class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        l = []
        if len(mat) * len(mat[0]) != r * c: return mat

        ans = [[0]*c for _ in range(r)]

        for i in range(len(mat)):
            for j in range(len(mat[0])): l.append(mat[i][j])
            
        v = 0
        for i in range(len(ans)):
            for j in range(len(ans[i])):
                ans[i][j] = l[v]
                v += 1
        return ans