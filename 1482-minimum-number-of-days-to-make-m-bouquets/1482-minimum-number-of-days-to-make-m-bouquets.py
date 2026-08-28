class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if(m*k > len(bloomDay)): return -1
        l, h = min(bloomDay), max(bloomDay)
        while(l<=h):
            mid = (l+h)//2
            cnt, bouquets = 0, 0
            for i in bloomDay:
                if(i <= mid): 
                    cnt+=1
                    if(cnt == k):
                        bouquets += 1
                        cnt = 0
                else: cnt = 0
            if(bouquets >= m): h = mid-1
            else: l = mid+1
        return l