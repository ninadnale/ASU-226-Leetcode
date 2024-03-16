class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length, count = 0, 0
        n = len(nums)
        count_map = {0:-1}
        
        for i in range(n):
            count += 1 if nums[i]==1 else -1
            if(count in count_map):
                max_length = max(max_length, i-count_map[count])
            else:
                count_map[count] = i
            
        return max_length