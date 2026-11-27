class Solution(object):
    def elevatorRequests(self, n, requests):
        """
        :type n: int
        :type requests: List[int]
        :rtype: int
        """
        ans = 0
        floor = 0
        for i in requests:
            if(i > floor):
                ans += i-floor
                floor = i
            elif(i < floor):
                ans += floor-i
                floor = i
        return ans