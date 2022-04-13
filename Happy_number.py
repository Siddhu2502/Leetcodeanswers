class Solution:
    def isHappy(n: int) -> bool:
        l = list()
        while(True and n != 1):
            k = 0
            while(n != 0):  
                t=n%10
                k += t**2  
                n=n//10
                
            n=k

            if (n in l):
                return False
            else:
                l.append(n)
                
        if(n == 1):
            return True
        return False

print(Solution.isHappy(1045))
print(Solution.isHappy(19))