class Solution:
    def isPalindrome(x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        if x[::-1] == x:
            return True

print(Solution.isPalindrome(x = 191))