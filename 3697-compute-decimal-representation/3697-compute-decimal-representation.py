class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:

        ans = []
        p = 1

        while n:

            d = n % 10

            if d:
                ans.append(d * p)

            p *= 10
            n //= 10

        return ans[::-1]