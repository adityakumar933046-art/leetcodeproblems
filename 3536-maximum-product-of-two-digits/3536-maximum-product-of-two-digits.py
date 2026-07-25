class Solution:
    def maxProduct(self, n: int) -> int:
        a = str(n)
        b = []
        for i in a:
            b.append(int(i))
        
        c = sorted(b)
        return c[-2]*c[-1]

        