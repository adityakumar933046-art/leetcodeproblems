class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        a = max(nums)
        c = min(nums)
        b =[]
        for i in range(c,a+1):
            if i not in nums:
                b.append(i)
        return b