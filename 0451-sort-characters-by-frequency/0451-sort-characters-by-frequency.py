class Solution:
    def frequencySort(self, s: str) -> str:
        char_map = {}
        for c in s:
            if c in char_map:
                char_map[c] += 1
            else:
                char_map[c] = 1
        
        sorted_chars = dict(sorted(char_map.items(), key=lambda x:x[1], reverse=True))
        answer = ""
        for c in sorted_chars:
            answer += c*sorted_chars[c]
        
        return answer