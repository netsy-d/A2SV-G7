class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiopQWERTYUIOP")
        row2 = set("asdfghjklASDFGHJKL")
        row3= set("zxcvbnmZXCVBNM")
        result =[]
        for word in words:
            if set(word).issubset(row1):
                result.append(word)
            elif set(word).issubset(row2):
                result.append(word)
            elif set(word).issubset(row3):
                result.append(word)
        return result
