class Solution:
    def average(self, salary: List[int]) -> float:
        Total = sum(salary) - min(salary) - max(salary)
        average_s = Total / (len(salary) -2)
    
        return average_s



        
        