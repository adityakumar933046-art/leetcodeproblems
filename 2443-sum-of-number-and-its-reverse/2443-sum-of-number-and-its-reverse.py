class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for i in range(0,num+1):
            rev = int(str(i)[::-1])
            if i +rev == num:            
                return True 
        return False     