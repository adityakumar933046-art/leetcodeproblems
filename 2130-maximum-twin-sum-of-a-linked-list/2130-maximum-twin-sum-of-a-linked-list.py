# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        a = []

        while head:
            a.append(head.val)
            head = head.next

        ans = 0
        n = len(a)

        for i in range(n // 2):
            ans = max(ans, a[i] + a[n - 1 - i])

        return ans
        