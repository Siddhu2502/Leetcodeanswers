class Solution:
    def largestPerimeter(nums: list[int]) -> int:   

        if len(nums) < 3: 
            return 0 

        nums.sort(reverse = True)
        for c in nums[2:]:
            if nums[1] + c > nums[0]:
                return nums[0] + nums[1] + c  
            nums[0], nums[1], c = nums[1], c, nums[0]  
        return 0

nums = [8, 24, 21, 20, 22, 21, 30, 20, 21, 16, 19, 22, 2, 22, 16, 8, 14, 14, 3, 2, 1, 24, 10, 13, 15, 2, 18, 24, 3, 15, 1, 24, 23, 25, 27, 18, 2, 12, 13, 8, 26, 10, 11, 1, 15, 27, 13, 28, 21, 13]

print(Solution.largestPerimeter(nums))