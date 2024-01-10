class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        firstList.extend(secondList)
        firstList.sort()
        inter = []
        for i in range(1, len(firstList)):
            if firstList[i-1][1] >= firstList[i][0]:
                inter.append([max(firstList[i-1][0], firstList[i][0]), min(firstList[i-1][1], firstList[i][1])])
                firstList[i][1] = max(firstList[i][1], firstList[i-1][1])
        return inter
        