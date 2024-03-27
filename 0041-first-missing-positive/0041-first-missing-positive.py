class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nextMin = 1
        for i in range(len(nums)):
            if(nums[i]<0):
                nums[i] = 0
        
        for i in range(len(nums)):
            idx = abs(nums[i])-1
            if(0<=idx<=len(nums)-1):
                if(nums[idx]>0):
                    nums[idx] = -1*nums[idx]
                elif(nums[idx]==0):
                    nums[idx] = -1*(len(nums)+1)
        print(nums)
        for i in range(len(nums)):
            if(nums[i]>=0):
                return i+1
        
        return len(nums)+1
            
