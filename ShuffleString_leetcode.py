class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        string = ""
        leng = max(indices)+1

        for i in range(leng):
            string+=s[indices.index(i)]

        return string
