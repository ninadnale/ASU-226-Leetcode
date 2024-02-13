class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        answer = ""
        for word in words:
            l, r = 0, len(word)-1
            while(l<=r and word[l]==word[r]):
                l += 1
                r -= 1
            if(r-l<=0):
                return word
        
        return answer