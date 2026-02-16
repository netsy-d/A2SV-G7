class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        
        for i in nums:
            i.sort()
        score = 0
        j = len(nums[0]) -1
        while j >=0:
            max = 0
            for i in nums:
                if max < i[j]:
                    max = i[j]
            score += max
            j-=1
        return score
