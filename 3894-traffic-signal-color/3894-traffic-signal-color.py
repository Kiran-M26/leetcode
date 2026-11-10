class Solution(object):
    def trafficSignal(self, timer):
        """
        :type timer: int
        :rtype: str
        """
        ans = ""
        if(timer == 0): ans = "Green"
        elif(timer == 30): ans = "Orange"
        elif(30 < timer <= 90): ans = "Red"
        else: ans = "Invalid"
        return ans