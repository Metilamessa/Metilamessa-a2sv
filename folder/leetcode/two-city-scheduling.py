class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        n = len(costs)
        for i in range(n):
            res = [costs[i][0]-costs[i][1],i]
            diff.append(res)           
        diff.sort()
        ans = 0
        for i in range(0,n//2):
            ans+= (costs[diff[i][1]][0])
        for i in range(n//2,n):
            ans+= (costs[diff[i][1]][1])
        
        return ans
           



        