class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[n] for n in nums]
        longest = []

        for i in reversed(range(len(nums))):
            for j in range(i+1, len(nums)):
                if(nums[j]%nums[i]==0):
                    tmp = [nums[i]] + dp[j]
                    dp[i] = tmp if len(tmp)>len(dp[i]) else dp[i]
            longest = dp[i] if len(dp[i]) > len(longest) else longest

        return longest