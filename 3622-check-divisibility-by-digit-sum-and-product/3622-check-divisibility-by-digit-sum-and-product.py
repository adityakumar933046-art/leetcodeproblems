class Solution:
    def checkDivisibility(self, n: int) -> bool:
        a =0
        b = 1
        for i in str(n):
            a+=int(i)
            b*=int(i)

        if n%(a+b)==0:
            return True
        else:
            return False

        