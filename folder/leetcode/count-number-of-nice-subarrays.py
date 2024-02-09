class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        def contain(nums, k):
            count=0
            left=0
            result=0

            for right in range(len(nums)):
                if nums[right] % 2 != 0:
                    k -= 1

                while k < 0:
                    if nums[left] % 2 != 0:
                        k += 1
                    left += 1

                result += right - left + 1

            return result

        return contain(nums, k) - contain(nums, k - 1)

