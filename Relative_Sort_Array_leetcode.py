class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr3 = []
        for i in arr2:
            for j in range(len(arr1)):
                if i == arr1[j]:
                    arr3.append(i)
                    arr1[j] = -1
        arr1.sort()
        for i in arr1:
            if i != -1:
                arr3.append(i)
        return arr3
        
