class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        lit=[]
        s="123456789"
        for length in range(2,10):
            for start in range(10-length):
                num = int(s[start:start+length])

                if low<= num<=high:
                    lit.append(num)
        lit.sort()
        return lit
        