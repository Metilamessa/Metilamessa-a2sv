class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque()
        for i, t in enumerate(tickets):
            q.append((t, i))

        count = 0
        while q:
            t, i = q.popleft()
            count+=1
            t -= 1
            if t > 0:
                q.append((t, i))
            if t == 0 and i==k:
                return count
        