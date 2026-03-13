class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        j = i+k
        n = len(nums)
        cur_sum = sum(nums[i:j])
        max_avg = float('-inf')
        if n <=1:
            return nums[0]/k
        while i <= n-k  and j <=n:
            if i!=0:
              cur_sum = cur_sum - nums[i-1] + nums[j-1] 
            cur_max = cur_sum/k
            max_avg = max(max_avg,cur_max)
            i+=1
            j+=1
        return max_avg

