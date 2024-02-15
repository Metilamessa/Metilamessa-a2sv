from collections import Counter

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        min_sum = 0
        n = len(answers)
        counter = Counter(answers)
        asked_before = set()

        for i in range(n):
            
            if counter[answers[i]]<=answers[i]+1:
                if answers[i] in asked_before:
                    continue
                else:
                    min_sum += (answers[i]+1)
                    asked_before.add(answers[i])
            else:
                if answers[i] in asked_before:
                    continue
                else:
                    div = ceil((counter[answers[i]])/(answers[i]+1))
                    min_sum += ((div)*(answers[i]+1))
                    asked_before.add(answers[i])
                print(counter[i])
        
        return min_sum