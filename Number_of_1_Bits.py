class Solution:
    def hammingWeight(n: int) -> int:
        c = 0
        while int(n):
            n &= n-1
            c += 1
        return c

print(Solution.hammingWeight(n=int(0x00000027)))