class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        ind = -1
        wl = list(word)
        for i in range(len(wl)):
            if(wl[i] == ch):
                ind = i
                break
        if(ind == -1): return word
        l, h = 0, ind
        while(l<h):
            wl[l], wl[h] = wl[h], wl[l]
            l += 1
            h -= 1
        return "".join(wl)