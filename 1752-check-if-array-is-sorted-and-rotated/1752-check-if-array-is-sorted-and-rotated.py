class Solution(object):
    def check(self, nums):
        n = len(nums)
        if nums[0] < nums[n-1]:
            last = nums[0]
            for ele in nums:
                if ele < last:
                    return False
                last = ele
            return True
        else:
            check = 0
            last = nums[0]
            for ele in nums:
                if ele < last:
                    check += 1
                if check > 1:
                    return False
                last = ele
            return True

        