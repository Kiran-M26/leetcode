class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sl = s.split(" ")
        for i in range(len(sl)):
            temp = list(sl[i])
            l, h = 0, len(temp)-1
            while(l<h):
                temp[l], temp[h] = temp[h], temp[l]
                l += 1
                h -= 1
            sl[i] = "".join(temp)
        return " ".join(sl)