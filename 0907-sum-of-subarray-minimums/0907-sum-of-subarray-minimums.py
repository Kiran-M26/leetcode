class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        mod = int(1e9+7)
        nse, psee = [0]*len(arr), [0]*len(arr)
        nstack, pstack = [], []
        for i in range(len(arr)-1, -1, -1):
            while(len(nstack)>0 and arr[nstack[-1]]>=arr[i]): nstack.pop()
            if(len(nstack)==0): nse[i] = len(arr)
            else: nse[i] = nstack[-1]
            nstack.append(i)

        for i in range(len(arr)):
            while(len(pstack)>0 and arr[pstack[-1]]>arr[i]): pstack.pop()
            if(len(pstack)==0): psee[i] = -1  
            else: psee[i] = pstack[-1]
            pstack.append(i)
        total = 0
        for i in range(len(arr)):
            left, right = i-psee[i], nse[i]-i
            total = (total + arr[i]*left*right)%mod 
        return total