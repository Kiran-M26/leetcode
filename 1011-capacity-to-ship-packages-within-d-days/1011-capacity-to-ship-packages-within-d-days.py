class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        l, h = max(weights), sum(weights)
        while(l<=h):
            limit = (l+h)//2
            initial_weight, initial_days = 0, 1
            for i in weights:
                if(initial_weight+i > limit):
                    initial_days += 1
                    initial_weight = 0
                initial_weight += i
            if(initial_days <= days): h = limit-1
            else: l = limit+1
        return l