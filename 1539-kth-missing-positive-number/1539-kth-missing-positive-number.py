class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        l, h = 0, len(arr)-1
        while(l<=h):
            m = (l+h)//2
            miss = arr[m] - (m+1)
            if(miss < k): l = m+1
            else: h = m-1
        return h+k+1