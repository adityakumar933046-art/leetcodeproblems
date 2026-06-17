class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        length = [0] * (n + 1)

        for i, ch in enumerate(s):
            cur = length[i]

            if 'a' <= ch <= 'z':
                length[i + 1] = cur + 1

            elif ch == '*':
                length[i + 1] = max(0, cur - 1)

            elif ch == '#':
                length[i + 1] = cur * 2

            else:  # %
                length[i + 1] = cur

        if k >= length[n]:
            return '.'

        for i in range(n - 1, -1, -1):

            ch = s[i]
            cur = length[i]
            nxt = length[i + 1]

            if 'a' <= ch <= 'z':

                if k == cur:
                    return ch

            elif ch == '*':

                pass

            elif ch == '#':

                if k >= cur:
                    k -= cur

            else:  # %

                k = cur - 1 - k

        return '.'