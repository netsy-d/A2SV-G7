#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        if len(b) > len(a):
            return False
        count_a = Counter(a)
        count_b = Counter(b)
        for num in b:
            if num not in count_a or count_b[num] > count_a[num]:
                return False
        return True
        
    
    
    
    
