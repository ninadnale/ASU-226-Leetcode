class Solution:
    def pivotInteger(self, n: int) -> int:
        if(n==1):
            return 1
        
        fullSum = n*(n+1)/2
        for i in range(n):
            partSum = i*(i+1)/2
            if(partSum == fullSum-partSum+i):
                return i

        return -1