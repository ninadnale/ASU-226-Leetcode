class Solution:
    def square(self, num):
        return num*num
    
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sorted_squares = []

        mid = 0

        for idx in range(n):
            mid = idx if (nums[idx]<abs(nums[mid])) else mid
        
        sorted_squares.append(self.square(nums[mid]))
        l, r = mid-1, mid+1

        while(l>=0 and r<n):
            if(abs(nums[l])<abs(nums[r])):
                sorted_squares.append(self.square(nums[l]))
                l -= 1
            else:
                sorted_squares.append(self.square(nums[r]))
                r += 1
        
        if(l>=0):
            for i in range(l, -1, -1):
                sorted_squares.append(self.square(nums[i]))
        if(r<n):
            for i in range(r, n):
                sorted_squares.append(self.square(nums[i]))

        return sorted_squares