class Solution:
    def makeGood(self, s: str) -> str:
        st = []
        
        for ch in s:
            st.append(ch)
            while(len(st)>=2 and abs(ord(st[-1])-ord(st[-2])) == 32):
                st.pop()
                st.pop()
        
        return ''.join(st)
    