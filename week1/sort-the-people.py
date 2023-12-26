class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        for i in range(1, n):
            current_name = names[i]
            current_height = heights[i]
            j = i - 1

            while j >= 0 and heights[j] < current_height:
                names[j+1] = names[j]
                heights[j+1] = heights[j]
                j -= 1

            names[j+1] = current_name
            heights[j+1] = current_height

        return names