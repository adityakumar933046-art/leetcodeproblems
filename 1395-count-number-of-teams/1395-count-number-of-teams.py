class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        ans = 0

        for j in range(n):
            leftLess = leftGreater = 0
            rightLess = rightGreater = 0

            for i in range(j):
                if rating[i] < rating[j]:
                    leftLess += 1
                else:
                    leftGreater += 1

            for k in range(j + 1, n):
                if rating[k] > rating[j]:
                    rightGreater += 1
                else:
                    rightLess += 1

            ans += leftLess * rightGreater
            ans += leftGreater * rightLess

        return ans