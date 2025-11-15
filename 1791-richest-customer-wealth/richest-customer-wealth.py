class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        result = []
        for i in range(0,len(accounts)):
            result.append(sum(accounts[i]))

        return max(result)
        