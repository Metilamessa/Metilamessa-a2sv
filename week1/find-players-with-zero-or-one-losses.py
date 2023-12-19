class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        players = set()
        losses = {}

        for match in matches:
            winner, loser = match
            players.add(winner)
            players.add(loser)

            if loser in losses:
                losses[loser] += 1
            else:
                losses[loser] = 1

        not_lost = [player for player in players if player not in losses]
        lost_once = [player for player, count in losses.items() if count == 1]

        return [sorted(not_lost), sorted(lost_once)]