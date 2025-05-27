class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = 0
        if not strs:
            return ""

        n = len(strs[0])

        for i in range(n):
            char = strs[0][i]

            for s in strs[1:]:
                if i >= len(s) or char != s[i]:
                    return strs[0][:i]
        return strs[0]
        
        # lcp = 0

        # if not strs:
        #     return ""

        # n = len(strs[0])

        # for i in range(n):
        #     char = strs[0][i]

        #     for s in strs[1:]:
        #         if i >= len(s) or char != s[i]:
        #             return strs[0][:i]
        
        # return strs[0]

            