class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        one_cnt = 0
        n = len(s)

        for bit in s:
            if(bit=='1'):
                one_cnt += 1
        
        answer = ""
        if(one_cnt==1):
            answer += "0"*(n-1)
            answer += "1"
        else:
            answer += "1"*(one_cnt-1)
            answer += "0"*(n-one_cnt)
            answer += "1"
        
        return answer
            