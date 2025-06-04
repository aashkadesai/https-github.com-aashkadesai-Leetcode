class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        n = len(words)
        res = []

        for word in words:
            res.append(word[0])
        
        result = "".join(res)

        return result == s