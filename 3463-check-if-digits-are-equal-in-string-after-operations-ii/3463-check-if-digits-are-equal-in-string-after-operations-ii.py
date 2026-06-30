class Solution:
    def hasSameDigits(self, s: str) -> bool:
        nums = list(map(int, s))
        n = len(nums)
        m = n - 2

        # Pascal mod 5 (0 <= n,k < 5)
        C5 = [
            [1,0,0,0,0],
            [1,1,0,0,0],
            [1,2,1,0,0],
            [1,3,3,1,0],
            [1,4,1,4,1]
        ]

        def comb_mod2(n, k):
            return 1 if (k & ~n) == 0 else 0

        def comb_mod5(n, k):
            res = 1
            while n or k:
                ni = n % 5
                ki = k % 5
                if ki > ni:
                    return 0
                res = (res * C5[ni][ki]) % 5
                n //= 5
                k //= 5
            return res

        # Chinese Remainder: mod2 + mod5 -> mod10
        def comb_mod10(n, k):
            a = comb_mod2(n, k)
            b = comb_mod5(n, k)
            for x in range(10):
                if x % 2 == a and x % 5 == b:
                    return x

        x = 0
        y = 0

        for i in range(m + 1):
            c = comb_mod10(m, i)
            x = (x + c * nums[i]) % 10
            y = (y + c * nums[i + 1]) % 10

        return x == y