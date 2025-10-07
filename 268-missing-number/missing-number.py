class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum_expected = n * (n + 1) // 2 
        sum_actual = sum(nums)            
        return sum_expected - sum_actual
        