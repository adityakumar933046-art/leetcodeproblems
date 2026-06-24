class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        mn = float('inf')

        for i in range(1, len(arr)):
            mn = min(mn, arr[i] - arr[i - 1])

        ans = []

        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == mn:
                ans.append([arr[i - 1], arr[i]])

        return ans