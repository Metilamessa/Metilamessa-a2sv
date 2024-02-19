class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:
        pre = []
        suf = []

        stack = [(0,-1)]
        for i in range(len(nums)):

            if nums[i] > stack[-1][0]:
                diff = i - stack[-1][1]
                pre.append(diff)
                stack.append((nums[i],i))

                
            else:
                while nums[i] <= stack[-1][0]:
                    stack.pop()
                diff = i - stack[-1][1]
                pre.append(diff)
                stack.append((nums[i],i)) 

        stack = [(0,len(nums))]
        for i in range(len(nums)-1,-1,-1):

            if nums[i] > stack[-1][0]:
                diff = stack[-1][1] - i
                suf.append(diff)
                stack.append((nums[i],i))
            
            else:
                    while nums[i] < stack[-1][0]:
                        stack.pop()
                    diff = stack[-1][1] - i
                    suf.append(diff)
                    stack.append((nums[i],i)) 


        suf = suf[::-1]   
        res = 0
        for i in range(len(pre)):
            res += suf[i] * pre[i] * nums[i]
        return res % (10**9 + 7)

