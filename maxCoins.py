class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        max_coins = 0
        i = len(piles)//3
        while i < len(piles):
            max_coins += piles[i] 
            i += 2
        return max_coins    

      

    
