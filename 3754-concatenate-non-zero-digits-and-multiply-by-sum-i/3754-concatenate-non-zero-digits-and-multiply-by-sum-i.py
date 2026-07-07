class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = str(n)

        digit_sum = sum(int(ch) for ch in s)

        num_str = "".join(ch for ch in s if ch != "0")

        num = int(num_str) if num_str else 0

        return digit_sum * num