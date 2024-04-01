class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        count = 0
        idx = len(s)-1
        
        while(idx>=0 and s[idx] != " "):
            count += 1
            idx -= 1

        return count