class Solution:
    def processStr(self, s: str) -> str: 
        res =[]
        for i in s:
            if i.isalpha():
                res.append(i)
            elif i == '#':
                res.extend(res)
            elif i == '*':
                if res:
                    res.pop()
            else:
                res.reverse()
        return "".join(res)
        