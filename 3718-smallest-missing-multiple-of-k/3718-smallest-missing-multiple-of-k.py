class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        a = sorted(nums)
        for i in range(1,len(a)+2):
            if i*k not in a:
                break
        return i*k


        