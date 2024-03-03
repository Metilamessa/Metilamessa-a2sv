class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort()
        prev = points[0]
        Tt = 1
        for s, e in points[1:]:
            if s > prev[1]:
                Tt += 1
                prev = [s, e]
            prev[1] = min(prev[1], e)
        return Tt

        