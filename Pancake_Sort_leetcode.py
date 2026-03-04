class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        bottom = len(arr)
        num = []
        def flip(k):
            for i in range(k//2):
                arr[i],arr[k-1-i] = arr[k-1-i],arr[i]
        for _ in range(len(arr)):
            max_index = 0
            for i in range(bottom):
                if arr[i] > arr[max_index]:
                    max_index = i
            flip(max_index+1)
            num.append(max_index+1)
            flip(bottom)
            num.append(bottom)
            bottom-=1
        return num
