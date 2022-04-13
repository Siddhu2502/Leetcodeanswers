class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:
        number = {}
        for count, num in enumerate(nums):
            if target-num in number:
                return number[target-num], count
            number[num] = count
            
            
print(Solution.twoSum(nums = [2,7,11,15],target = 9))
        