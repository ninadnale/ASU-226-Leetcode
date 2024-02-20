class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        for i in nums:
            total += i
        
        return int((n+1)*(n)/2 - total)