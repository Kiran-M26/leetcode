class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        sl = list(s)
        v = []
        for i in s:
            if i in ["a","e","i","o","u","A","E","I","O","U"]: v.append(i)
        l, r = 0, len(v)-1
        while(l<r):
            v[l], v[r] = v[r], v[l]
            l += 1
            r -= 1
        cnt = 0
        for i in range(len(sl)):
            if sl[i] in ["a","e","i","o","u","A","E","I","O","U"]:
                sl[i] = v[cnt]
                cnt += 1
        return "".join(sl)