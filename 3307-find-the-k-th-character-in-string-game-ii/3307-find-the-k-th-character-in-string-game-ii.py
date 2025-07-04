class Solution(object):
    def kthCharacter(self, k, operations):
        n, i = 1, 0
        while n < k:
            n <<= 1
            i += 1

        shift = 0
        while n > 1:
            half = n >> 1
            if k > half:
                k -= half
                shift += operations[i - 1]
            n = half
            i -= 1

        return chr((shift % 26) + ord('a'))
