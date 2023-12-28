class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = Counter(nums1)
        intersection = []
        for num in nums2:
            if num in counter and counter[num] > 0:
                intersection.append(num)
                counter[num] -= 1
        return intersection
            