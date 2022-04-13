class Solution:
    def tribonacci(n: int) -> int:

        f = {0:0, 1:1, 2:1}
        for i in range(3,n+1):
            f[i] = f[i-1]+f[i-2]+f[i-3]    
            
        return f[n]