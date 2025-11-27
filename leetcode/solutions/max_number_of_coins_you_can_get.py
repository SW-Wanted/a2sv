class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        
        total, left, right = 0, 0, n - 1

        while left < right:
            total += piles[right - 1]
            right -= 2
            left += 1
            
        return total