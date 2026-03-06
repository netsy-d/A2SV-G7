class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
       scored =  sorted(score,reverse=True)
       d = {}
       l =[]
       for i in range(len(score)):
         if i == 0:
            d[scored[i]]  ="Gold Medal"
         elif i ==1:
            d[scored[i]] = "Silver Medal"
         elif i ==2:
            d[scored[i]] ="Bronze Medal"
         else:
            d[scored[i]] = str(i+1)
       for i in score:
         l.append(d[i])
       return l    
