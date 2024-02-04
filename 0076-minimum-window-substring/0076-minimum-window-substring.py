class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if(s=="" or t=="" or m==0 or n==0 or m<n):
            return ""
        
        start, end = 0, 0
        minLen = float('inf')
        start_index = 0

        t_map = [0] * 128
        for ch in t:
            t_map[ord(ch)] += 1

        while end<len(s):
            if(t_map[ord(s[end])])>0:
                n -= 1
            t_map[ord(s[end])] -= 1
            end += 1

            while n==0:
                if(end-start < minLen):
                    start_index = start
                    minLen = end-start
                
                if(t_map[ord(s[start])]) == 0:
                    n += 1
                t_map[ord(s[start])] += 1
                start += 1
            
        return "" if minLen==float('inf') else s[start_index:start_index+minLen]