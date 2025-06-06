class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(part) for part in version1.split('.')]
        v2 = [int(part) for part in version2.split('.')]

        max_len = max(len(v1), len(v2))
        v1 += [0] * (max_len - len(v1))
        v2 += [0] * (max_len - len(v2))

        for a, b in zip(v1, v2):
            if a > b:
                return 1
            elif a < b:
                return -1
        return 0