class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []


        if len(nums) == 1:
            return [nums.copy()]


        for i in range(len(nums)):
            p = nums.pop(0)
            prms = self.permute(nums)


            for prm in prms:
                prm.append(p)
            res.extend(prms)
            nums.append(p)
        return res
