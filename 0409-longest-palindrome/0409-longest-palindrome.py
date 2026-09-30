class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}
        for i in s:
            if i in freq: freq[i] += 1
            else: freq[i] = 1
        ans, odd = 0, False
        for i in freq.values():
            if(i%2 == 0): ans += i
            else:
                ans += i-1
                odd = True
        return ans+1 if(odd == True) else ans