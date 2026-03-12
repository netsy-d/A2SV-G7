class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        wide = 0
        current_width=0
        for i in range(len(points)-1):
            current_width = points[i+1][0] - points[i][0]
            wide = max(wide,current_width) 
        return wide
      
