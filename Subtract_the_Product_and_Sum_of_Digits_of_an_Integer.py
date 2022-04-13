class Solution:
    def subtractProductAndSum(n: int) -> int:
        p = 1
        s = 0
        while int(n):
            p *= int(n%10)
            s += s + int(n%10)
            n = n//10
            ans = (p-s)
        return ans

print(Solution.subtractProductAndSum(n = 9845494))