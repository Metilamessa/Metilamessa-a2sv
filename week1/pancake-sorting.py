class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:   
        flips = []  

        for i in range(len(arr), 1, -1):
            max_idx = arr.index(i)  

            if max_idx != i - 1:              
                arr = arr[:max_idx+1][::-1] + arr[max_idx+1:]
                flips.append(max_idx + 1)
                arr = arr[:i][::-1] + arr[i:]
                flips.append(i)

        return flips
        