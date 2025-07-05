class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        freq = Counter(arr)
        ans = -1
        for val, cnt in freq.items():
            if val == cnt:
                ans = max(ans, val)
        return ans