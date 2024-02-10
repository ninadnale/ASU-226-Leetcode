class Solution:
    def getPalindromeCount(self, s:str, l:int, r:int):
        cnt = 0
        while(l>=0 and r<len(s) and s[l]==s[r]):
            cnt += 1
            l -= 1
            r += 1
        
        return cnt
    
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        
        for i in range(0, n):
            count += self.getPalindromeCount(s, i, i)
            count += self.getPalindromeCount(s, i, i+1)
        
        return count