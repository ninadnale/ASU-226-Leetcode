class Solution:
    def tribonacci(self, n: int) -> int:
        tn, tn1, tn2 = 0, 1, 1
        if(n==0):
            return 0
        if(n==1 or n==2):
            return 1
        
        for i in range(3, n+1):
            temp = tn2 + tn1 + tn
            tn2, tn1, tn = temp, tn2, tn1
        
        return tn2