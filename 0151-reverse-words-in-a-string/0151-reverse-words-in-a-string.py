class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.strip().split()
        word.reverse()
        return " ".join(word)