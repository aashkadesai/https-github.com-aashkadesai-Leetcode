from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = defaultdict(list)

        # for s in strs:
        #     count = [0] * 26

        #     for c in s:
        #         count[ord(c) - ord("a")] += 1
            
        #     res[tuple(count)].append(s)
            
        # return list(res.values())

        anagram_map = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            anagram_map[key].append(word)
        
        return list(anagram_map.values())