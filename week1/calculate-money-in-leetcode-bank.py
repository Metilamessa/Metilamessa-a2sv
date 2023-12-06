class Solution:
    def totalMoney(self, n: int) -> int:
        full_weeks = n // 7
        remaining_days = n % 7
        total = 0
        
        
        total += 28 * full_weeks + 7 * (full_weeks - 1) * full_weeks // 2
        
        
        for i in range(remaining_days):
            total += full_weeks + i + 1
        
        return total