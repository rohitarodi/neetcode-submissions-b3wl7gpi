class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 
        right = max(piles)
        res = right
        # k = 1
        while left <= right :
            k = (left + right) // 2
            total_hours = sum(math.ceil(p/k) for p in piles)
            if total_hours > h:
                left = k + 1
            else:
                res = k
                right = k - 1
        return res