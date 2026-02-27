class Solution: 
    def selectionSort(self, arr):
        #code here
        n = len(arr)
        for i in range(n-1):
            min_value = i 
            for j in range(i+1,n):
                if arr[min_value] > arr[j]:
                    min_value = j
            arr[i],arr[min_value] = arr[min_value] , arr[i]
        
        return " ".join(str(arr))
