class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_kid = max(candies)
        ne = []
        result = []
        for i in range(0,len(candies)):
            ne.append(candies[i] + extraCandies)
    
        for i in range(0,len(ne)):
            if ne[i] >= max_kid:
                result.append(True)
            else:
                result.append(False)

        return result
        