class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        fs, ss = min(prices[0], prices[1]), max(prices[0], prices[1])
        for i in range(2, len(prices)):
            if(prices[i] <= fs): 
                ss = fs
                fs = prices[i]
            elif(prices[i] > fs and prices[i] < ss): ss = prices[i]
        return money if(fs+ss > money) else money-(fs+ss)