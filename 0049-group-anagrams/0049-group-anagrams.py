class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = collections.defaultdict(list)
        for word in strs:
            char_map = [0] * 26
            for w in word:
                char_map[ord('z') - ord(w)] += 1
            
            anagram_map[tuple(char_map)].append(word)
        
        return anagram_map.values()