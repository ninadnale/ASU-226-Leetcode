class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        l, r = 0, n-1
        
        while(l<r):
            left_char = s[l]
            right_char = s[r]
            if(left_char!=right_char):
                break
            while(l<n and s[l]==right_char):
                l += 1
            while(r>0 and s[r]==left_char):
                r -= 1
            if(l==r):
                return 1
            elif(r<l):
                return 0
        
        return r-l+1