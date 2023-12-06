class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1 = ""
        for i in word1:
            s1 += word1[i]
            i+=1
        s2 = ""
        for i in word2:
            s2 += word2[i]
            i+=1
            if s1 == s2:
                return true
            else:
                return false
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1 = ""
        for i in word1:
            s1 += i

        s2 = ""
        for j in word2:
            s2 += j

        return s1 == s2