#Power of two , basic py solution for the problem
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and  (n&(n-1) )==0
        