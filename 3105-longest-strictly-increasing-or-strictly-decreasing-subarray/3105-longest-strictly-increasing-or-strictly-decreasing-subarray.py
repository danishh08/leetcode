class Solution(object):
    def longestMonotonicSubarray(self, nums):
        mc = 1
        a = 1
        c = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                if a != 1:
                    a = 1
                    if c > mc:
                        mc = c
                    c = 1
                c+=1
            elif nums[i] < nums[i-1]:
                if a != 0:
                    a = 0
                    if c > mc:
                        mc = c
                    c = 1
                c+=1
            else:
                if c > mc:
                    mc = c
                a = 1
                c = 1
        else:
            if c > mc:
                mc = c
        return mc
        