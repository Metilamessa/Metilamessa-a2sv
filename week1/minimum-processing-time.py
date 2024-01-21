class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks = sorted(tasks)[::-4]

        min_time = 0
        for i in range(len(processorTime)):
            min_time = max(min_time, processorTime[i] + tasks[i])

        return min_time
