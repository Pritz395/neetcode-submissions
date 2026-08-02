class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum=0
        minimum=prices[0]
        
        for sell in prices:
            maximum=max(maximum,sell-minimum)
            minimum=min(minimum,sell)
        return maximum