class Solution:
    def checkValidString(self, s: str) -> bool:
        p1 = 0
        p2 = 0
        for i in range(len(s)):
            if s[i] == '(':
                p1 += 1
                p2 += 1
            elif s[i] == ')':
                p1 -= 1
                p2 -= 1
            elif s[i] == '*':
                p1 += 1
                p2 -= 1
            if p1 < 0:
                return False
            if p2 < 0:
                p2 = 0
        return p2 == 0