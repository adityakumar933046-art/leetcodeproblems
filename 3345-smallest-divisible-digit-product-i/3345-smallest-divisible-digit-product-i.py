class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
    
            digit_product = 1
            
    
            for digit in str(n):
                digit_product *= int(digit)
            
    
            if digit_product % t == 0:
                return n
            
            
            n += 1