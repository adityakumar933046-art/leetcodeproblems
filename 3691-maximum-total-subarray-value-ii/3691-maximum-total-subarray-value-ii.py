class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Sparse tables
        LOG = (n).bit_length()

        st_max = [nums[:]]
        st_min = [nums[:]]

        j = 1
        while (1 << j) <= n:
            prev_max = st_max[j - 1]
            prev_min = st_min[j - 1]

            size = n - (1 << j) + 1

            cur_max = [0] * size
            cur_min = [0] * size

            half = 1 << (j - 1)

            for i in range(size):
                cur_max[i] = max(prev_max[i], prev_max[i + half])
                cur_min[i] = min(prev_min[i], prev_min[i + half])

            st_max.append(cur_max)
            st_min.append(cur_min)
            j += 1

        def value(l: int, r: int) -> int:
            length = r - l + 1
            p = length.bit_length() - 1

            mx = max(st_max[p][l], st_max[p][r - (1 << p) + 1])
            mn = min(st_min[p][l], st_min[p][r - (1 << p) + 1])

            return mx - mn

        # max heap
        heap = []

        for l in range(n):
            v = value(l, n - 1)
            heapq.heappush(heap, (-v, l, n - 1))

        ans = 0

        for _ in range(k):
            neg_v, l, r = heapq.heappop(heap)

            ans += -neg_v

            if r > l:
                nr = r - 1
                heapq.heappush(
                    heap,
                    (-value(l, nr), l, nr)
                )

        return ans