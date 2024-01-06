class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        def distance(point):
            return math.pow(point[0], 2) + math.pow(point[1], 2)
        
        def quick(left, right):
            if left >= right: return

            pivot = random.randint(left, right)
            points[pivot], points[right] = points[right], points[pivot]
            pivot_distance = distance(points[right])
            
            pointer = left
            for i in range(left, right):
                if distance(points[i]) <= pivot_distance:
                    points[i], points[pointer] = points[pointer], points[i]
                    pointer += 1
            points[pointer], points[right] = points[right], points[pointer]
            
            if pointer > k: 
                quick(left, pointer - 1)
            elif pointer < k:
                quick(pointer + 1, right)

        quick(0, len(points) - 1)
        
        return points[:k]
