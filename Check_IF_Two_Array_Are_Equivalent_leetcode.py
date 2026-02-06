class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        i=j=0
        x=y=0
        while i < len(word1) and j < len(word2):
             if word1[i][x] != word2[j][y]:
                 return False
             x +=1
             y+=1
             if x == len(word1[i]):
                x = 0
                i+=1
             if y == len(word2[j]):
                y = 0
                j +=1
        return i == len(word1) and j == len(word2)
