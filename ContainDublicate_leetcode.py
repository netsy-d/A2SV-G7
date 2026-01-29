class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count_nums= Counter(nums)
        for num in count_nums:
            if count_nums[num] >= 2:
                return True
        return False
