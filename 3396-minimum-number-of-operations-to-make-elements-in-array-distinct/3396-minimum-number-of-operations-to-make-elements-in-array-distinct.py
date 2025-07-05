class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ops = 0
        while len(set(nums)) != len(nums):
            nums = nums[3:]
            ops += 1
        return ops