class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        ans = 0
        for i in range(len(items)):
            if(ruleKey == "type" and items[i][0] == ruleValue): ans += 1
            if(ruleKey == "color" and items[i][1] == ruleValue): ans += 1
            if(ruleKey == "name" and items[i][2] == ruleValue): ans += 1
        return ans