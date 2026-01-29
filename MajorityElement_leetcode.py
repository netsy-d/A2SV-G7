class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_nums= Counter(nums)
        n= len(nums)
        for num in  count_nums:
            if count_nums[num] >n//2:
                return num
