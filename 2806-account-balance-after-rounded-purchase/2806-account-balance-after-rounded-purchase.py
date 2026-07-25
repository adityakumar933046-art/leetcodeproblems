class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        a = str(purchaseAmount)
        if int(a[-1]) in range(0,5) :
            c = purchaseAmount- int(a[-1])
        else:
            c = purchaseAmount+(10-int(a[-1]))
        return 100-c

        