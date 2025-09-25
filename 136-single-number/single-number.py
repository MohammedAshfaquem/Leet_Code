class Solution(object):
    def singleNumber(self,nums):
        for i in nums:
            return 2 * sum(set(nums)) - sum(nums)
        