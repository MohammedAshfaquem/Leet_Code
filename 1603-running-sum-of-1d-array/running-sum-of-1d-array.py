class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        count = 0
        for i in range(0,len(nums)):
            count += nums[i]
            result.append(count)

        return result
        