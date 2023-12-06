class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        result = []
        
        for word in words:
            if self.isSingleRow(word.lower(), rows):
                result.append(word)
        
        return result
    
    def isSingleRow(self, word: str, rows: List[str]) -> bool:
        for row in rows:
            if all(char in row for char in word):
                return True
        
        return False
        