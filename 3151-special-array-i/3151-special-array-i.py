class Solution:
    def isArraySpecial(self, A):
        return all((a & 1) != (b & 1) for a, b in zip(A, A[1:]))