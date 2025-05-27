class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = Counter(s)
        # print (s_dict)
        t_dict = Counter(t)
        # print(t_dict)

        return s_dict==t_dict