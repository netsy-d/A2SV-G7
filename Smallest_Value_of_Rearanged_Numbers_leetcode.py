class Solution:
    def smallestNumber(self, num: int) -> int:
        
       count = 0
       if num == 0:
         return 0
       elif num <0:
         num = -num
         num = sorted(str(num),reverse=True)
         num = int("".join(num))
         return  -num
       else:
        num = sorted(str(num))
        counter = num.count("0")
        num = num[counter:counter+1] + ["0"]* counter + num[counter+1:] 
        num = int("".join(num))
        return num

         
