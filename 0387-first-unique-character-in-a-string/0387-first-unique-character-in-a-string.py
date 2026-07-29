class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i  in range(len(s)):
            a = s.count(s[i])
            if a==1:
                return i
                break
        return -1