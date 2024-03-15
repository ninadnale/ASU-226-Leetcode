class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for num in nums:
            if(num!=0):
                product *= num
            else:
                zero_count += 1
        
        product_except_self = []
        if(zero_count>1):
            return [0] * len(nums)
        for num in nums:
            if(zero_count==1):
                if(num==0):
                    product_except_self.append(product)
                else:
                    product_except_self.append(0)
            else:
                product_except_self.append(product//num)
        
        return product_except_self