class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        
        for i in range(len(arr)): 
            if arr[0] != 1:
                arr[0] = 1       
            if abs(arr[i-1]-arr[i]) <=1:
                continue
            elif abs(arr[i-1]-arr[i]) > 1:
                arr[i]= arr[i-1]+1
        return max(arr)
                     