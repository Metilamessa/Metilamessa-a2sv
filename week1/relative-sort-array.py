class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        list1 = []
        list2 = []
        count = [0] * 1001
        
       
        for num in arr1:
            count[num] += 1
        
       
        for num in arr2:
            list1.extend([num] * count[num])
            count[num] = 0
        
        for i in range(len(arr1)):
            if arr1[i] not in arr2:
                list2.append(arr1[i])
                list2.sort()
            
        
        ans = list1 + list2
        return ans      