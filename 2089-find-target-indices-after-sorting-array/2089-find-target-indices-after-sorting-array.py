class Solution:
    def targetIndices(self, nums, target):
        countLess = 0
        countEqual = 0

        for num in nums:
            if num < target:
                countLess += 1
            elif num == target:
                countEqual += 1

        return [i for i in range(countLess, countLess + countEqual)]
 