class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        
        for num in nums:
            if num > 0:
                positive.append(num)
            else:
                negative.append(num)
        
        rearranged_elements = []
        n = len(positive)
        
        for i in range(n):
            rearranged_elements.append(positive[i])
            rearranged_elements.append(negative[i])
        
        return rearranged_elements