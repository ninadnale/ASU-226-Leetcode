class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        
        s_map = assist.map_word(s)
        t_map = assist.map_word(t)
        
        return s_map == t_map

class assist:
    def map_word(s: str) -> list:
        dict1 = {}
        l1 = []
        count = 0
        for i in s:
            if i not in dict1:
                dict1[i] = count
                count = count+1
                l1.append(dict1[i])
            else:
                l1.append(dict1[i])
        return l1