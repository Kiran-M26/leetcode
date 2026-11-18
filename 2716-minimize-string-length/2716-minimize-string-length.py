class Solution(object):
    def minimizedStringLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        visited = []
        for i in s:
            if i in visited: continue
            else: visited.append(i)
        return len(visited)