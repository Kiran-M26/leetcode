class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 1
        R_count, L_count = 0, 0
        for i in s:
            if((R_count == L_count) and R_count>0 and L_count>0):
                ans += 1
                R_count, L_count = 0, 0
            if(i == "R"): R_count += 1
            elif(i == "L"): L_count += 1
        return ans