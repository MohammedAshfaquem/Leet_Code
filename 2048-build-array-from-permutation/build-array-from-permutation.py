class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        for i in range(0,len(nums)):
            result.append(nums[nums[i]])
        return result
        