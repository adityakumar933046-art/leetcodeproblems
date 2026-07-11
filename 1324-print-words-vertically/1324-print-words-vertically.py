class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        m = max([len(i) for i in words])

        lit= []
        for i in range(m):
            curr =""
            for word in words:
                if i < len(word):
                    curr += word[i]
                else:
                    curr += " "
            lit.append(curr.rstrip())
        return lit    
            