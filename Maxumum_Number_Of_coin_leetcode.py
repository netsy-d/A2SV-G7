class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort()
        value = 0
        i = -2
        for _ in range(n//3):
            value += piles[i]
            i -=2
        return value
        

