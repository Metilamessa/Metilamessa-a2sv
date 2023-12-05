 
class Solution:
    def compare_words(self, word1, word2, order_dict) -> bool:
        n1, n2 = len(word1), len(word2)

        for i in range(min(n1, n2)):
            if word1[i] != word2[i]:
                if order_dict[word1[i]] > order_dict[word2[i]]:
                    return False
                else:
                    return True

        return n1 <= n2

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {c: i for i, c in enumerate(order)}

        for i in range(1, len(words)):
            if not self.compare_words(words[i - 1], words[i], order_dict):
                return False
        
        return True