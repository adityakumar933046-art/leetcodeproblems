class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort(key=lambda x: x[1])

        ends = [ride[1] for ride in rides]

        m = len(rides)
        dp = [0] * (m + 1)

        for i in range(1, m + 1):

            start, end, tip = rides[i - 1]

            profit = end - start + tip

            j = bisect_right(ends, start) - 1

            dp[i] = max(
                dp[i - 1],
                dp[j + 1] + profit
            )

        return dp[m]
                
        