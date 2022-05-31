class Solution:
    def longestCommonPrefix(strs: list[str]) -> str:
        r = ''
        for v in range(len(min(strs))):
            test_c = strs[0][v]
            if all(a[v] == test_c for a in strs):
                r += test_c
            else:
                return r
        return r   

print(Solution.longestCommonPrefix(strs = ["atgct","agct"]))