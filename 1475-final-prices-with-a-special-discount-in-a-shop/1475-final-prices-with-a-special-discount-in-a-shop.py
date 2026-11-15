class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(prices)):
            m = prices[i]
            c = False
            for j in range(i+1, len(prices)):
                if(prices[j] <= m):
                    m = prices[j]
                    c = True
                    break
            if(c == True): ans.append(prices[i]-m)
            else: ans.append(prices[i])
        return ans