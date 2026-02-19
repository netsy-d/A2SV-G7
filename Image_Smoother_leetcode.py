class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n = len(img)
        m = len(img[0])
        result = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                total  = 0
                count = 0
                for x in range(max(i-1,0),min(i+2,n)):
                    for y in range(max(j-1,0),min(j+2,m)):
                        total+= img[x][y]
                        count+=1
                result[i][j] = total//count
        return result
