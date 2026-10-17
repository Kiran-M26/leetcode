class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        f, s, t = ["q","w","e","r","t","y","u","i","o","p"], ["a","s","d","f","g","h","j","k","l"], ["z","x","c","v","b","n","m"]
        c = -1
        for word in words:
            if word[0].lower() in f: c = f
            elif word[0].lower() in s: c = s
            else: c = t
            for j in range(len(word)):
                if word[j].lower() not in c:
                    break
                if(j == len(word)-1): ans.append(word)

        return ans
