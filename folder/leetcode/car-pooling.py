class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        trips.sort(key=lambda x: x[2])
        n = trips[-1][-1]

        
        ans = [0]* (n+1)

        for numPassengers, frm , to in trips:
            ans[frm] += numPassengers
            ans[to] -= numPassengers
 
        if ans[0] > capacity:
            return False

        for i in range(1,n):
            ans[i] += ans[i-1]
        
            if ans[i] > capacity:
                return False
                         
        return True
