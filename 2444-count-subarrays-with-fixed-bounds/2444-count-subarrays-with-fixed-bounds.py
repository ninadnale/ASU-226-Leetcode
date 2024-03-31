class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        bad_idx = min_idx = max_idx = -1

        for r, num in enumerate(nums):
            if(not minK <= num <= maxK):
                bad_idx = r
            
            if(num==minK):
                min_idx = r
            if(num==maxK):
                max_idx = r
            
            count += max(0, min(min_idx, max_idx) - bad_idx)
        
        return count