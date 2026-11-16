class Solution(object):
    def reverseByType(self, s):
        """
        :type s: str
        :rtype: str
        """
        alph = 'abcdefghijklmnopqrstuvwxyz'
        sl = list(s)
        i, j = 0, len(sl)-1
        while(i<j):
            if (sl[i] in alph) and (sl[j] in alph):
                sl[i], sl[j] = sl[j], sl[i]
                i += 1
                j -= 1
            elif sl[i] not in alph:
                i += 1
            else:
                j -= 1
        i, j = 0, len(sl)-1
        while(i<j):
            if(sl[i] not in alph) and (sl[j] not in alph):
                sl[i], sl[j] = sl[j], sl[i]
                i += 1
                j -= 1
            elif(sl[i] in alph):
                i += 1
            else: j -= 1
        return "".join(sl)