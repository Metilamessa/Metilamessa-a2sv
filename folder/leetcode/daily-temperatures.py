class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
 
        queue = deque()
        res = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            if not queue:
                queue.appendleft(i)
                res[i] = 0
            else:
                while queue and temperatures[i] >= temperatures[queue[0]]:
                    queue.popleft()

                if not queue:
                    res[i] = 0
                else:
                    res[i] = queue[0] - i

                queue.appendleft(i)

        return res



        