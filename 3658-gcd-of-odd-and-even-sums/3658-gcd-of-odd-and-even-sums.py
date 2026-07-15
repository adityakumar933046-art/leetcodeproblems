from math import gcd

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd = n * n
        even = n * (n + 1)

        while even:
            odd, even = even, odd % even

        return odd