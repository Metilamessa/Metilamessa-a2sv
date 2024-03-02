class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []

        for num in nums2[::-1]:
            while stack and stack[-1] <= num:
                stack.pop()

            if not stack:
                next_greater[num] = -1
            else:
                next_greater[num] = stack[-1]

            stack.append(num)

        result = []
        for num in nums1:
            result.append(next_greater[num])

        return result