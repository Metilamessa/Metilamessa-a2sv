class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
       
        steps = 0
        currCapacity = capacity
        for idx in range(len(plants)):
            steps += 1
            currCapacity -= plants[idx]
            if idx <= (len(plants) -2) and currCapacity < plants[idx + 1]:
                steps += 2 * (idx+1)
                currCapacity = capacity

        return steps

            
