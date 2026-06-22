class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        a = Counter(text)
        return min(a['b'],a['a'],a['l']//2,a['o']//2,a['n'])
