class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def advance(i: int) -> int:
            return (i + nums[i]) % len(nums)

        if len(nums) < 2:
            return False

        for start_index, start_num in enumerate(nums):
            if start_num == 0:
                continue

            slow = start_index
            fast = advance(slow)

            while start_num * nums[fast] > 0 and start_num * nums[advance(fast)] > 0:
                if slow == fast:
                    if slow == advance(slow):
                        break
                    return True
                slow = advance(slow)
                fast = advance(advance(fast))

            slow = start_index
            sign = start_num

            while sign * nums[slow] > 0:
                next_index = advance(slow)
                nums[slow] = 0
                slow = next_index

        return False
