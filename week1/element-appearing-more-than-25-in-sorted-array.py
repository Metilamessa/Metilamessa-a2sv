class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        window_size = len(arr) // 4 + 1

        for i in range(len(arr) - window_size + 1):
            if arr[i] == arr[i + window_size - 1]:
                return arr[i]

        return -1  
        