class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        top_num = nums[0]
        count = 0
        for i in range(n):
            if nums[i]==top_num:
                count += 1
            else:
                count -= 1
                if(count<=0):
                    top_num = nums[i]
                    count = 1
        
        return top_num