class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        result = [0] * n

    
        totalBalls = 0
        totalOperations = 0
        for i in range(n):
            result[i] += totalOperations
            totalBalls += int(boxes[i])
            totalOperations += totalBalls

   
        totalBalls = 0
        totalOperations = 0
        for i in range(n - 1, -1, -1):
            result[i] += totalOperations
            totalBalls += int(boxes[i])
            totalOperations += totalBalls

        return result

        