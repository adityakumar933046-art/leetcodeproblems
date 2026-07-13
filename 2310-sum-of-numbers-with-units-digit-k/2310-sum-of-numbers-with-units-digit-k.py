class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0

        for x in range(1, 11):
            if x * k % 10 == num % 10 and x * k <= num:
                return x

        return -1
        