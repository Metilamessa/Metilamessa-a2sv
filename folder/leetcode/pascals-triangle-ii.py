class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        def helper(index):

            if index == 1:
                return [1, 1]

            arr = helper(index - 1)
            
            ans = [0] * (index + 1)
            ans[0], ans[-1] = 1, 1

            for i in range(1, len(ans) -1):
                ans[i] = arr[i -1] + arr[i]

            return ans

        return helper(rowIndex)






