class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        import math

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans = math.inf
        last_seen = {}

        for i, card in enumerate(cards):
            if card in last_seen:
                ans = min(ans, i - last_seen[card] + 1)
            last_seen[card] = i

        return -1 if ans == math.inf else ans

        