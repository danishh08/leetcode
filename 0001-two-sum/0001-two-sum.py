class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=len(nums)
        arr=[]
        for i in range (l):
            for j in range(1,l):
                if nums[i]+nums[j]==target and i!=j:
                    arr.append(i)
                    arr.append(j)
                    return arr