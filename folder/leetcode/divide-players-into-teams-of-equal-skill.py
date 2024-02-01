class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        num_players = len(skill)
        total_skill = sum(skill)
        team_skill = total_skill // (num_players // 2)
        total_pairs = 0
        
        skill_count = Counter(skill)

        for s, freq in skill_count.items():
            required_skill = team_skill - s
            if skill_count[required_skill] != freq:
                return -1
            total_pairs += s * required_skill * freq

        return total_pairs // 2
