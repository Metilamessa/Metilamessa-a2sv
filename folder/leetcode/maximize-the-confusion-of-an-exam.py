class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_length = 0
        max_count = 0
        current_count = collections.Counter()

        left_pointer = 0
        for right_pointer, char in enumerate(answerKey):
            current_count[char == 'T'] += 1
            max_count = max(max_count, current_count[char == 'T'])
            while max_count + k < right_pointer - left_pointer + 1:
                current_count[answerKey[left_pointer] == 'T'] -= 1
                left_pointer += 1
            max_length = max(max_length, right_pointer - left_pointer + 1)

        return max_length
        