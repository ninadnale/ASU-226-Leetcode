class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            if(nums[abs(nums[i])-1]<0):
                answer.append(abs(nums[i]))
            else:
                nums[abs(nums[i])-1] = -1 * nums[abs(nums[i])-1]
        
        return answer