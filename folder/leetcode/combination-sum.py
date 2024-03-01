class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        
        def backtrack(start, path, path_sum):
            
            if path_sum == target:
                ans.append(path[:])
                return
            
            for indx in range(start, len(candidates)):
                if candidates[indx] + path_sum > target:
                    continue
                
                path.append(candidates[indx])
                backtrack(indx, path, path_sum + candidates[indx])
                path.pop()
        
        backtrack(0, [], 0)
        return ans