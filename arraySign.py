class Solution:
    def arraySign(nums: list[int]) -> int:
        
        product = 1
        for i in nums:
            product *= i
        if product > 0:
            return 1
        if product < 0:
            return -1
        return 0

list1 = [10, 20, 10, 30, 40, 40]
print(Solution.arraySign(list1))