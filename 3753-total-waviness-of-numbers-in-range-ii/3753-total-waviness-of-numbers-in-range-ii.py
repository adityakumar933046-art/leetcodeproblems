from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(n: int) -> int:
            if n <= 0:
                return 0

            s = str(n)
            m = len(s)

            @lru_cache(None)
            def dfs(pos, tight, started, prev2, prev1, cnt):
                if pos == m:
                    return (1, 0)  # one number, zero extra waviness

                limit = int(s[pos]) if tight else 9

                totalWays = 0
                totalWav = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if not started and d == 0:
                        ways, wav = dfs(
                            pos + 1,
                            ntight,
                            False,
                            10,
                            10,
                            0
                        )
                        totalWays += ways
                        totalWav += wav
                    else:
                        if not started:
                            ways, wav = dfs(
                                pos + 1,
                                ntight,
                                True,
                                10,
                                d,
                                1
                            )
                            totalWays += ways
                            totalWav += wav
                        else:
                            add = 0

                            if cnt >= 2:
                                if (prev1 > prev2 and prev1 > d) or \
                                   (prev1 < prev2 and prev1 < d):
                                    add = 1

                            if cnt == 1:
                                nprev2, nprev1, ncnt = prev1, d, 2
                            else:
                                nprev2, nprev1, ncnt = prev1, d, 2

                            ways, wav = dfs(
                                pos + 1,
                                ntight,
                                True,
                                nprev2,
                                nprev1,
                                ncnt
                            )

                            totalWays += ways
                            totalWav += wav + add * ways

                return totalWays, totalWav

            return dfs(0, True, False, 10, 10, 0)[1]

        return solve(num2) - solve(num1 - 1)
        