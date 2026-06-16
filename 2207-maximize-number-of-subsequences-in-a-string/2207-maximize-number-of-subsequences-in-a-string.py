class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        a,b = pattern[0],pattern[1]
        c =0
        d =0
        ans =0
        for ch in text:
            if ch ==b:
                ans+=c
                d+=1
            if ch==a:
                c+=1
        return ans + max(c,d)
