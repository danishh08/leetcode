class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        top_k = sorted(indexed_nums, key=lambda x: -x[0])[:k]
        top_k.sort(key=lambda x: x[1])
        return [num for num, idx in top_k]
