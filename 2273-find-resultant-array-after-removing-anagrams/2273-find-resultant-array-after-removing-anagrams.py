class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        lit =[]
        for i in words:
            if not lit or sorted(lit[-1])!=sorted(i):
                lit.append(i)
        return lit            

        