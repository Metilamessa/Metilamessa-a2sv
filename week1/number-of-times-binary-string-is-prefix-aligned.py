class Solution:
  def numTimesAllBlue(self, flips: List[int]) -> int:
    pre_aligned = 0
    right = 0

    for i, flip in enumerate(flips):
      right = max(right, flip)
      if right == i + 1:
        pre_aligned += 1
    
    return pre_aligned