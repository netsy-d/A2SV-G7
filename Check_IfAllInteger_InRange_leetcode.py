class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = set()
        for start, end in ranges:
            for num in range(start, end+1):
                if left <= num <= right:
                    covered.add(num)
        for num in range(left, right+1):
            if num not in covered:
                return False
        return True
