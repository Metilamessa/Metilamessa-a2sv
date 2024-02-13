class Solution:
    def balancedString(self, s: str) -> int:
        extra_chars = Counter(s) - Counter({'Q': len(s) // 4, 'W': len(s) // 4, 'E': len(s) // 4, 'R': len(s) // 4})
        if not extra_chars:
            return 0
        
        min_length = len(s)
        char_indices = defaultdict(list)
        for i, char in enumerate(s):
            char_indices[char].append(i)
            if any(len(char_indices[k]) < v for k, v in extra_chars.items()):
                continue
            min_length = min(min_length, i - min(char_indices[k][-v] for k, v in extra_chars.items()) + 1)
        return min_length
