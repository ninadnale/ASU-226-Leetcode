class Solution:
    def maxSum(self, arr, k, dp, start):
        n = len(arr)
        if(start>=n):
            return 0
        elif(dp[start]!=-1):
            return dp[start]
        
        currMax, ans = 0, 0
        for i in range(start, min(start+k, n)):
            currMax = max(currMax, arr[i])
            ans = max(ans, currMax*(i-start+1) + self.maxSum(arr, k, dp, i+1))
        
        dp[start] = ans
        return ans
    
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [-1 for i in range(len(arr))]
        
        return self.maxSum(arr, k, dp, 0)
        