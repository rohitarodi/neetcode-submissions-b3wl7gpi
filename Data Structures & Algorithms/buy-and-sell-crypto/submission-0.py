class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #brute force
        max_profit = []
        for i in prices:
            for j in prices[prices.index(i):]:
                diff = j - i
                max_profit.append(diff)
        max_num = max(max_profit)
        if max_num > 0 :
            return max_num
        else :
            return 0