class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occur = {char: i for i, char in enumerate(s)}
        partition = []
        start = end = 0
        
        for i, char in enumerate(s):
            end = max(end, last_occur[char])
            if i == end:
                partition.append(end - start + 1)
                start = i + 1
        
        return partition