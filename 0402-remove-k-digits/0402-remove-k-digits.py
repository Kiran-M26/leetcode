class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if(len(num) == k): return "0"
        stack = []
        pos = 0
        for _ in range(len(num)):
            if(len(stack) == 0): 
                stack.append(num[pos])
                pos += 1
                continue
            while(len(stack)>0 and int(stack[-1])>int(num[pos]) and k>0): 
                stack.pop()
                k -= 1
            stack.append(num[pos])
            pos += 1

        while(k>0): 
            stack.pop()
            k -= 1
        nz = 0
        nzd = 0
        for i in range(len(stack)):
            if(stack[i] != "0"): nzd += 1

        for i in range(len(stack)):
            if(stack[i] != "0"):
                nz = i
                break
        return "".join(stack[nz:]) if(nzd > 0) else "0"