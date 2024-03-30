class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def subarraysWithKAtMost(nums: List[int], k):
            freq_map = {}
            l = 0
            count = 0

            for r, num in enumerate(nums):
                if(num not in freq_map):
                    freq_map[num] = 1
                    while(len(freq_map)>k):
                        freq_map[nums[l]] -= 1
                        if(freq_map[nums[l]]==0):
                            freq_map.pop(nums[l])
                        l += 1
                else:
                    freq_map[num] += 1
                
                count += r-l+1
            return count
        
        return subarraysWithKAtMost(nums, k) - subarraysWithKAtMost(nums, k-1)