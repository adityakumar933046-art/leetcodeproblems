class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)

        ans = 1

        if 1 in cnt:
            if cnt[1] % 2 == 0:
                ans = cnt[1] - 1
            else:
                ans = cnt[1]

        for x in list(cnt.keys()):
            if x == 1:
                continue

            cur = x
            length = 0

            while cnt[cur] >= 2:
                length += 2
                if cur > 10 ** 9:
                    break
                cur = cur * cur

            if cnt[cur] >= 1:
                length += 1
            else:
                length -= 1

            ans = max(ans, length)

        return ans