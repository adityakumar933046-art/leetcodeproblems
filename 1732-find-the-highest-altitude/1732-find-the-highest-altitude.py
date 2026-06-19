class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a=[0]
        b=0
        for i in range(len(gain)):
            b+=int(gain[i])
            a.append(b)
        return max(a)
             

        