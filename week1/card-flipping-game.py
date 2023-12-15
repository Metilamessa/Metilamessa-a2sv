class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        card_set = set(fronts + backs)
        min_good = float('inf')

        for num in fronts + backs:
            if num not in card_set:
                continue

            is_good = True
            for i in range(len(fronts)):
                if fronts[i] == backs[i] == num:
                    is_good = False
                    break

            if is_good:
                min_good = min(min_good, num)

        return min_good if min_good != float('inf') else 0